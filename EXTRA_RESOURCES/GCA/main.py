"""
                                    FelipedelosH
                                        2024

    :WARNING: DONT EXECUTE THIS SCRIPT IN SPRINGBOOT PROJECT ROOT :WARNING:

SQL code generator:
    sql.sql in output folder


Spring boot Code Generator:
    API (getAll)
    USECASE (GetAllEntity)
    ENTITIES
    JPA-DAO
    MAPPERS
"""
import os
import xml.etree.ElementTree as ET

def loadFile(PATH):
    data = ""

    try:
        with open(PATH, "r", encoding="UTF-8") as f:
            data = f.read()
    except:
        pass

    return data



_PATH_DRAWIO_CLASES_FILE = "input/class.drawio" # ruta de nuestro archivo de clases
_LOGS_ = ""
_template_sql = loadFile("templates/sql.txt")
_template_api = loadFile("templates/getAllClassAPI.txt")
_template_entity = loadFile("templates/ENTITY.txt")
_template_use_case_param = loadFile("templates/getAllClassUseCaseParam.txt")
_template_use_case_contract = loadFile("templates/getAllClassUseCase.txt")
_template_use_case_implementation = loadFile("templates/getAllClassUseCaseIml.txt")
_template_dao_repository = loadFile("templates/DAORepository.txt")
_template_dao_service = loadFile("templates/DAOService.txt")
_template_dao_entiry = loadFile("templates/DAOEntity.txt")
tree = ET.parse(_PATH_DRAWIO_CLASES_FILE) # Usamos la libreria para construir el XML
root = tree.getroot() # Inicializamos el xml


def saveLOG(_type, date, hour, information):
    pass


def getAllClasesAttribs():
    """
    Enter XML with Diagram Of class And return dic
    key = "name of class" ; value = "+-att:type;"
    """
    _data = {}
    _className = ""

    for iterMxCell in root.findall(".//mxCell[@value]"):    
        _value = iterMxCell.attrib.get('value')
        _parent = iterMxCell.attrib.get('parent')

        if _value != "":
            try:
                if _parent == "1":
                    _className = _value
                    _data[_className] = []
                else:
                    _data[_className].append(_value)
            except:
                print("Error in value: ", _className, _value)


    return _data
_DATA = getAllClasesAttribs()


def formatDataToSQL():
    """
    Enter a dic with:
        key: class name
        data: array "+-att:type;"
    """
    sql = ""

    for itterData in _DATA:
        _table_name = str(itterData).lower()
        _attribs = getAllAttribsToSQL(_DATA[itterData])

        sql = sql + f"{_template_sql.replace("<TABLENAME>", _table_name).replace("<ATTRIBS>", _attribs)}\n"

    return sql

def getAllAttribsToSQL(arrAttribs):
    """
    Enter array str with information ["+-att:type;", "+-att:type;"... "+-att:type;"] 
    and return posgresql row
    examples:
        + id:Strig; = id character varying(255) PRIMARY KEY,
        + qty:Double; = qty DOUBLE PRECISION,
        + age:int; = age integer
    """
    attribs = ""
    _pk = "<var_name> <type> PRIMARY KEY,"

    for iterAttrins in arrAttribs:
        _sql_attrib = str(iterAttrins).replace(" ", "")
        _sql_attrib = _sql_attrib.replace("+", "")
        _sql_attrib = _sql_attrib.replace("-", "")
        _sql_attrib = _sql_attrib.replace(";", "")
        if "):" in _sql_attrib:
            #print("es un método: ", _sql_attrib)
            continue

        _sql_attrib = _sql_attrib.split(":")
        
        _name_var = _sql_attrib[0]
        _type_var = _sql_attrib[1]

        if _name_var == "id":
            _temp = _pk.replace("<var_name>", _name_var)
            _temp = _temp.replace("<type>", registerTypeOfSQLVars(_type_var))
            attribs = attribs + f"{_temp}\n"
            continue

        attribs = attribs + f"\t{_name_var} {registerTypeOfSQLVars(_type_var)},\n"

    # Erase last comma
    attribs = attribs[:-2]

    return attribs


def registerTypeOfSQLVars(type):
    dic = {
        "String" : "character varying(255)",
        "Double" : "DOUBLE PRECISION",
        "int" : "integer"
    }

    try:
        return dic[type]
    except:
        return dic["String"]
    


def getAllAttribsToJava(arrAttribs):
    """
    Enter array str with information ["+-att:type;", "+-att:type;"... "+-att:type;"] 
    and return JAVA VARS
    examples:
        + id:Strig; = public String id;,
        + qty:Double; = public Double qty;,
        + age:int; = public String id;
    """
    attribs = ""

    for iterAttrins in arrAttribs:
        _var_attrib = str(iterAttrins).replace(" ", "")

        _encapsutlation = _var_attrib[0]

        if _encapsutlation == "-":
            _encapsutlation = "private"
        else:
            _encapsutlation = "public"

        _var_attrib = str(_var_attrib).replace(" ", "")
        _var_attrib = _var_attrib.replace("+", "")
        _var_attrib = _var_attrib.replace("-", "")
        _var_attrib = _var_attrib.replace(";", "")


        _var = _var_attrib.split(":")[0]

        # If is method abort
        if "(" in _var and ")" in _var:
            continue

        _type = _var_attrib.split(":")[1]

        if not isRegisterTypeOfJavaVars(_type):
            continue

        attribs = attribs + f"\t{_encapsutlation} {_type} {_var};\n"


    return attribs


def getAllAttribsToJPA(arrAttribs):
    """
    Enter array str with information ["+-att:type;", "+-att:type;"... "+-att:type;"] 
    and return JAVA  JPA VARS
    examples:
        + id:Strig;
        + qty:Double;
        + age:int; 

            @Id
            @Column(name = "id")
            private String id;
            
            @Column(name = "qty")
            private Double qty;
    """
    attribs = ""
    for iterAttrins in arrAttribs:
        _var_attrib = str(iterAttrins).replace(" ", "")

        _encapsutlation = _var_attrib[0]

        if _encapsutlation == "-":
            _encapsutlation = "private"
        else:
            _encapsutlation = "public"

        _var_attrib = str(_var_attrib).replace(" ", "")
        _var_attrib = _var_attrib.replace("+", "")
        _var_attrib = _var_attrib.replace("-", "")
        _var_attrib = _var_attrib.replace(";", "")


        _var = _var_attrib.split(":")[0]

        # If is method abort
        if "(" in _var and ")" in _var:
            continue

        _type = _var_attrib.split(":")[1]

        if not isRegisterTypeOfJavaVars(_type):
            continue

        if _var == "id":
            attribs = attribs +  f"\t@Id\n\t@Column(name = \"{_var}\")\n" + f"\t{_encapsutlation} {_type} {_var};\n\n"
        else:
            attribs = attribs +  f"\t@Column(name = \"{_var}\")\n" + f"\t{_encapsutlation} {_type} {_var};\n\n"

        
    return attribs


def getJavaConstructorWithVars(vars):
    """
    Enter a java vars:

        public String id;
        public String username;
        public String contrasena;
        public String name;
        public int age;

    and return constructor:
            public User(String id,String username,String contrasena,String name,int age){
                this.id = id;
                this.username = username;
                this.contrasena = contrasena;
                this.name = name;
                this.age = age;
            }
    """
    _construct = _emptyConstruct = f"\tpublic {_entity}(<ARGS>){{\n<THIS.ARGS>\n\t}}"
    
    _setVars = [] # Catch all vars
    for itterVar in vars.split("\n"):
        if str(itterVar).strip() != "":
            _var = str(itterVar).lstrip()
            _var = _var.replace("public ", "")
            _var = _var.replace("private ", "")
            _var = _var.replace(";", "")
            _setVars.append(_var)

    # Args to enter in contruct
    if len(_setVars) == 0:
        _construct = _construct.replace("<ARGS>", "")
        return _construct
    else:
        _args = ""
        for i in _setVars:
            _args = _args + i + ","
        
        _args = _args[:-1]
        _construct = _construct.replace("<ARGS>", _args)

        _thisargs = ""
        for i in _setVars:
            _nameVar = str(i).split(" ")[1]
            _thisargs = _thisargs + f"\t\tthis.{_nameVar} = {_nameVar};\n"

        _thisargs = _thisargs[:-1]

        _construct = _construct.replace("<THIS.ARGS>", _thisargs)

    return _construct


def getJavaSetterAndGetters(vars):
    """
    Enter a java vars:
        public String id;
        public String username;

    retrun getters and setters:

        public String getId(){
            return this.id;
        }

        public setId(String id){
        ...
    """
    setters_getters = ""
    _setVars = [] # Catch all vars
    for itterVar in vars.split("\n"):
        if str(itterVar).strip() != "":


            _var = str(itterVar).replace("public", "")
            _var = _var.replace("private", "")
            _var = _var.replace(";", "")
            _var = _var.lstrip()
            _type =  _var.split(" ")[0]

            if not isRegisterTypeOfJavaVars(_type):
                continue

            _var = _var.split(" ")[-1]

            # If is method abort
            if "(" in _var and ")" in _var:
                continue

            _newStters = f"\tpublic void set{_var[0].upper()+_var[1:]}({_type} {_var}){{\n\t\tthis.{_var} = {_var};\n\t}}\n"
            setters_getters = setters_getters + _newStters + "\n"
            _newGetter = f"\tpublic {_type} get{_var[0].upper()+_var[1:]}({_type} {_var}){{\n\t\treturn this.{_var};\n\t}}\n"
            setters_getters = setters_getters + _newGetter + "\n"

    return setters_getters


def getJavaToString(vars):
    """
    Enter a java vars:
        public String id;
        public String username;

        retrun toString java method
    """
    to_string = """
    @Override
    public String toString() {
        return <JSON>;
    }
    """
    _visual_json = ""
    _setVars = [] # Catch all vars
    for itterVar in vars.split("\n"):
        if str(itterVar).strip() != "":
            _var = str(itterVar).replace("public", "")
            _var = _var.replace("private", "")
            _var = _var.replace(";", "")
            _var = _var.lstrip()
            _type =  _var.split(" ")[0]

            if not isRegisterTypeOfJavaVars(_type):
                continue

            _var = _var.split(" ")[-1]

            # If is method abort
            if "(" in _var and ")" in _var:
                continue

            if _type == "int": 
                _visual_json = _visual_json + "\t" + f"\t\t\"\\\"{_var}\\\":\" " + f" + {_var} + " + "\"\\\",\"" + " + \n"
            else:
                _visual_json = _visual_json + "\t" + f"\t\t\"\\\"{_var}\\\": \\\"\"" + f" + {_var} + " + "\"\\\",\"" + " + \n"

    # The json Starts with {
    _visual_json = "\t\"{\" +\n"  + _visual_json
    

    #The last option dont end to pattern need to end }
    len_pattern = len(' + "\"," +\n')
    _visual_json = _visual_json[0:-len_pattern]
    _visual_json = _visual_json + "\n\t\t\"}\""

    return to_string.replace("<JSON>", _visual_json)


def getIDTypeToJava(vars):
    """
    Enter a str vars:
        public String id;
        public String username;
        public int age;

        retrun String
    
    """
    data = ""

    if "id" in vars:
        for i in vars.split("\n"):
            if str(i).strip() != "":
                _itterVar = str(i)
                _itterVar = str(_itterVar).replace("public", "")
                _itterVar = _itterVar.replace("private", "")
                _itterVar = _itterVar.replace(";", "")
                _itterVar = _itterVar.lstrip()
                _type = _itterVar.split(" ")[0]
                _itterVar = _itterVar.split(" ")[-1]

                if _itterVar == "id":
                    if isRegisterTypeOfJavaVars(_type):
                        return _type

    return data



def isRegisterTypeOfJavaVars(type):
    arr = ["String", "Double", "int"]
    return type in arr


def createFolderEntity(entity):
    try:
        _statusFOLDERENTITY = os.path.exists(f"output/{entity}")
        if not _statusFOLDERENTITY:
            os.mkdir(f"output/{entity}")
    except:
        print(f"ERROR TO CREATE {entity} FOLDER")


def createFolderGetAllEntityUseCase(entity):
    try:
        _statusFOLDERENTITY = os.path.exists(f"output/{entity}/getAll{entity}UseCase")
        if not _statusFOLDERENTITY:
            os.mkdir(f"output/{entity}/getAll{entity}UseCase")
    except:
        print(f"ERROR TO CREATE {i} FOLDER")


def createFolderEntityDAO(entity):
    try:
        _statusFOLDERENTITY = os.path.exists(f"output/{entity}/{entity}DAO")
        if not _statusFOLDERENTITY:
            os.mkdir(f"output/{entity}/{entity}DAO")
    except:
        print(f"ERROR TO CREATE {entity} FOLDER")


#SAVE FILES
for i in _DATA:
    createFolderEntity(i)
    createFolderGetAllEntityUseCase(i)
    createFolderEntityDAO(i)
    # Names of Class And Objects
    _entity = i
    _APIClassName = f"get{i}ApiRest"
    _useCaseFolderName = f"getAll{i}UseCase"
    _useCaseName = _useCaseFolderName[0].upper() + _useCaseFolderName[1:]
    _useCaseParamName = f"GetAll{i}Param"
    _useCaseContractName = f"GetAll{i}UseCase"
    _useCaseVarName = _useCaseName.lower()
    _useCaseImplClassName = f"GetAll{i}UseCaseImpl"
    _useCaseServiceName = f"{i}Service"
    _useCaseServiceVarName = _useCaseServiceName.lower()
    _daoRepositoryClassName = f"{i}Repository"
    _daoServiceClassName = f"{i}Service"
    _daoEntityClassName = f"{i}Entity"

    # TEMPLATES.JAVA
    ENTITY = _template_entity[:]
    ENTITY = ENTITY.replace('<ENTITY>', _entity)
    _vars = getAllAttribsToJava(_DATA[i])
    ENTITY = ENTITY.replace('<VARS>', _vars)
    _emptyConstruct = f"\tpublic {_entity}(){{\n\t}}"
    ENTITY = ENTITY.replace('<EMPTY-CONSTRUCT>', _emptyConstruct)
    _FullConstruct =  getJavaConstructorWithVars(_vars)
    ENTITY = ENTITY.replace('<FULL-CONSTRUCT>', _FullConstruct)
    _setters_getters = getJavaSetterAndGetters(_vars)
    ENTITY = ENTITY.replace('<SETTERS-GETTERS>', _setters_getters)
    _to_string = getJavaToString(_vars)
    ENTITY = ENTITY.replace('<TO-STRING>', _to_string)

    #SAVE ENTITY
    with open(f"output/{i}/{_entity}.java", "w", encoding="UTF-8") as f:
        f.write(ENTITY)


    API = _template_api[:]
    API = API.replace('<USECASEFOLDER>', _useCaseFolderName)
    API = API.replace('<ENTITY>', _entity)
    API = API.replace('<USECASE>', _useCaseName)
    API = API.replace('<USECASEPARAM>', _useCaseName+"Param")
    API = API.replace('<usecase>', _useCaseVarName)

    #SAVE API
    with open(f"output/{i}/{_APIClassName}.java", "w", encoding="UTF-8") as f:
        f.write(API)


    USE_CASE_PARAM = _template_use_case_param[:]
    USE_CASE_PARAM = USE_CASE_PARAM.replace('<ENTITY>', i)
    USE_CASE_PARAM = USE_CASE_PARAM.replace('<USECASEFOLDER>', _useCaseFolderName)

    #SAVE USE CASE PARAM
    with open(f"output/{i}/getAll{i}UseCase/{_useCaseParamName}.java", "w", encoding="UTF-8") as f:
        f.write(USE_CASE_PARAM)


    USE_CASE_CONTRACT = _template_use_case_contract[:]
    USE_CASE_CONTRACT = USE_CASE_CONTRACT.replace('<ENTITY>', i)
    USE_CASE_CONTRACT = USE_CASE_CONTRACT.replace('<USECASEFOLDER>', _useCaseFolderName)

    #SAVE USE CASE CONTRACT
    with open(f"output/{i}/getAll{i}UseCase/{_useCaseContractName}.java", "w", encoding="UTF-8") as f:
        f.write(USE_CASE_CONTRACT)

    USE_CASE = _template_use_case_implementation[:]
    USE_CASE = USE_CASE.replace('<ENTITY>', i)
    USE_CASE = USE_CASE.replace('<USECASEFOLDER>', _useCaseFolderName)
    USE_CASE = USE_CASE.replace('<SERVICE>', _useCaseServiceName)
    USE_CASE = USE_CASE.replace('<service>', _useCaseServiceVarName)


    #SAVE USE CASE IMPL
    with open(f"output/{i}/getAll{i}UseCase/{_useCaseImplClassName}.java", "w", encoding="UTF-8") as f:
        f.write(USE_CASE)



    DAO_REPOSITORY = _template_dao_repository[:]
    DAO_REPOSITORY = DAO_REPOSITORY.replace('<ENTITY>', i)
    _typeID = getIDTypeToJava(_vars)
    DAO_REPOSITORY = DAO_REPOSITORY.replace('<ID-TYPE>', _typeID)


    #SAVE DAO Repository
    with open(f"output/{i}/{i}DAO/{_daoRepositoryClassName}.java", "w", encoding="UTF-8") as f:
        f.write(DAO_REPOSITORY)


    DAO_SERVICE = _template_dao_service[:]
    DAO_SERVICE = DAO_SERVICE.replace('<ENTITY>', i)
    DAO_SERVICE = DAO_SERVICE.replace('<REPOSITORY>', _daoRepositoryClassName)
    _daoRepositoryVarName = _daoRepositoryClassName.lower()
    DAO_SERVICE = DAO_SERVICE.replace('<repository>', _daoRepositoryVarName)


    #SAVE DAO Service
    with open(f"output/{i}/{i}DAO/{_daoServiceClassName}.java", "w", encoding="UTF-8") as f:
        f.write(DAO_SERVICE)


    DAO_ENTITY = _template_dao_entiry[:]
    DAO_ENTITY = DAO_ENTITY.replace('<ENTITY>', i)
    _varsEntity = getAllAttribsToJPA(_DATA[i])
    DAO_ENTITY = DAO_ENTITY.replace('<VARS>', _varsEntity)

    #SAVE DAO Entity
    with open(f"output/{i}/{i}DAO/{_daoEntityClassName}.java", "w", encoding="UTF-8") as f:
        f.write(DAO_ENTITY)





# SAVE SQL FILE
with open("output/sql.sql", "w", encoding="UTF-8") as f:
    f.write(formatDataToSQL())