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
import datetime

_LOGS_ = f"PYTHON:STARTED\n"
def saveLOG(_type, date, hour, information):
    global _LOGS_
    _LOGS_ = _LOGS_ + _type + "|" + date + "|" + hour + "|" + information + "\n"

def getDateYYYYMMDD():
    return str(datetime.datetime.now().strftime("%Y-%m-%d"))

def getHourHHMM():
    return str(datetime.datetime.now().strftime("%H%M"))

def loadFile(PATH):
    data = ""

    try:
        with open(PATH, "r", encoding="UTF-8") as f:
            data = f.read()
    except:
        pass

    return data

_PATH_DRAWIO_CLASES_FILE = "input/class.drawio" # ruta de nuestro archivo de clases
_template_sql = loadFile("templates/sql.txt")
_template_api = loadFile("templates/getAllClassAPI.txt")
_template_entity = loadFile("templates/ENTITY.txt")
_template_use_case_param = loadFile("templates/getAllClassUseCaseParam.txt")
_template_use_case_contract = loadFile("templates/getAllClassUseCase.txt")
_template_use_case_implementation = loadFile("templates/getAllClassUseCaseIml.txt")
_template_dao_repository = loadFile("templates/DAORepository.txt")
_template_dao_service = loadFile("templates/DAOService.txt")
_template_dao_entiry = loadFile("templates/DAOEntity.txt")
_template_mapper_entiry = loadFile("templates/MapperEntity.txt")
tree = ET.parse(_PATH_DRAWIO_CLASES_FILE) # Usamos la libreria para construir el XML
root = tree.getroot() # Inicializamos el xml


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
                saveLOG("ERROR:FATAL", getDateYYYYMMDD(), getHourHHMM(), f"Error in value: {str(_className)} {str(_value)}")


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
        "int" : "integer",
        "List<String>" : "String"
    }

    try:
        return dic[type]
    except:
        saveLOG("ERROR:SQL:VAR", getDateYYYYMMDD(), getHourHHMM(), f"TRY TO SEARCH A {str(type)} in registerTypeOfSQLVars(type) AND NOT FOUND")
        return dic["String"]
    


def getAllAttribsToJava(arrAttribs):
    """
    Enter array str with information ["+-att:type;", "+-att:type;"... "+-att:type;"] 
    and return JAVA VARS
    examples:
        + id:Strig; = public String id;
        + qty:Double; = public Double qty;
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
            _newGetter = f"\tpublic {_type} get{_var[0].upper()+_var[1:]}(){{\n\t\treturn this.{_var};\n\t}}\n"
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


    # Number or Str
    if _type == "int":
        _visual_json = _visual_json + "\n\t\t\"}\""
    else:
        _visual_json = _visual_json + " \"\\\"\" + " + "\n\t\t\"}\""

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


def getJavaMapperToJPAEntity(entity, vars):
    """
    Enter a str vars and entity className:
        public String id;
        public String username;
        public int age;

        retrun

            public static XYZEntity toEntity(XYZ xyz) {
                return new XYZEntity(xyz.getId(), xyz.getUsername(), xyz.getAge());
            }
    """
    _toEntity = """
    public static <ENTITY>Entity toEntity(<ENTITY> <entity>) {
        return new <ENTITY>Entity(<GET-VARS>);
    }
    """

    _setVars = [] # Catch all vars
    for itterVar in vars.split("\n"):
        if str(itterVar).strip() != "":
            _var = str(itterVar).lstrip()
            _var = _var.replace("public ", "")
            _var = _var.replace("private ", "")
            _var = _var.replace(";", "")
            _var = _var.split(" ")[-1]
            _setVars.append(_var)

    _toEntity = _toEntity.replace("<ENTITY>", entity)
    _toEntity = _toEntity.replace("<entity>", entity.lower())

    final_get_vars = ""
    for i in _setVars:
        _getVar = f"get{str(i)[0].upper() +str(i)[1:]}()"
        final_get_vars = final_get_vars + f"{entity.lower()}." + _getVar + ","


    # Erase last comma
    final_get_vars = final_get_vars[:-1]
   
    _toEntity = _toEntity.replace("<GET-VARS>", final_get_vars)


    return _toEntity


def getJavaMapperToDomainEntity(entity, vars):
    """
    Enter a str vars and entity className:
        public String id;
        public String username;
        public int age;

        retrun

            public static  XYZ toDomain(XYZEntity xyz) {
                return new XYZ(xyz.getId(), xyz.getUsername(), xyz.getAge());
            }
    """
    _toEntity = """
    public static <ENTITY> toDomain(<ENTITY>Entity <entity>) {
        return new <ENTITY>(<GET-VARS>);
    }
    """

    _setVars = [] # Catch all vars
    for itterVar in vars.split("\n"):
        if str(itterVar).strip() != "":
            _var = str(itterVar).lstrip()
            _var = _var.replace("public ", "")
            _var = _var.replace("private ", "")
            _var = _var.replace(";", "")
            _var = _var.split(" ")[-1]
            _setVars.append(_var)

    _toEntity = _toEntity.replace("<ENTITY>", entity)
    _toEntity = _toEntity.replace("<entity>", entity.lower())

    final_get_vars = ""
    for i in _setVars:
        _getVar = f"get{str(i)[0].upper() +str(i)[1:]}()"
        final_get_vars = final_get_vars + f"{entity.lower()}." + _getVar + ","


    # Erase last comma
    final_get_vars = final_get_vars[:-1]
   
    _toEntity = _toEntity.replace("<GET-VARS>", final_get_vars)


    return _toEntity

def createFolderEntity(entity):
    try:
        _statusFOLDERENTITY = os.path.exists(f"output/{entity}")
        if not _statusFOLDERENTITY:
            os.mkdir(f"output/{entity}")
    except:
        saveLOG("FOLDER-NOT-CREATE:ERROR", getDateYYYYMMDD(), getHourHHMM(), f"ERROR TO CREATE A FOLDER {entity}")


def createFolderGetAllEntityUseCase(entity):
    try:
        _statusFOLDERENTITY = os.path.exists(f"output/{entity}/getAll{entity}UseCase")
        if not _statusFOLDERENTITY:
            os.mkdir(f"output/{entity}/getAll{entity}UseCase")
    except:
        saveLOG("FOLDER-NOT-CREATE:ERROR", getDateYYYYMMDD(), getHourHHMM(), f"ERROR TO CREATE A FOLDER USECASE{entity}")


def createFolderEntityDAO(entity):
    try:
        _statusFOLDERENTITY = os.path.exists(f"output/{entity}/{entity}DAO")
        if not _statusFOLDERENTITY:
            os.mkdir(f"output/{entity}/{entity}DAO")
    except:
        saveLOG("FOLDER-NOT-CREATE:ERROR", getDateYYYYMMDD(), getHourHHMM(), f"ERROR TO CREATE A FOLDER DAO{entity}")


def createJavaFILE_ENTITY(e_name, e_vars):
    """
    Enter a name of entity and its vars.
    creates Entity.java File
    """
    ENTITY = _template_entity[:]
    ENTITY = ENTITY.replace('<ENTITY>', e_name)
    ENTITY = ENTITY.replace('<VARS>', e_vars)
    _emptyConstruct = f"\tpublic {e_name}(){{\n\t}}"
    ENTITY = ENTITY.replace('<EMPTY-CONSTRUCT>', _emptyConstruct)
    _FullConstruct =  getJavaConstructorWithVars(e_vars)
    ENTITY = ENTITY.replace('<FULL-CONSTRUCT>', _FullConstruct)
    _setters_getters = getJavaSetterAndGetters(e_vars)
    ENTITY = ENTITY.replace('<SETTERS-GETTERS>', _setters_getters)
    _to_string = getJavaToString(e_vars)
    ENTITY = ENTITY.replace('<TO-STRING>', _to_string)

    #SAVE ENTITY
    with open(f"output/{e_name}/{e_name}.java", "w", encoding="UTF-8") as f:
        f.write(ENTITY)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {e_name}.java FILE")



def createJavaFILE_API(e_name, useCaseFolderName, useCaseClassName, useCaseVarName, useCaseParamClassName):
    """
    Enter:
        entity name, name of usecase folder name, name of contract use case & param.
    Creates:
        API.java
    """
    _APIClassName = f"get{e_name}ApiRest"
    API = _template_api[:]
    API = API.replace('<ENTITY>', e_name)
    API = API.replace('<USECASEFOLDER>', useCaseFolderName)
    API = API.replace('<USECASE>', useCaseClassName)
    API = API.replace('<usecase>', useCaseVarName)
    API = API.replace('<USECASEPARAM>', useCaseParamClassName)
    
    #SAVE API
    with open(f"output/{e_name}/{_APIClassName}.java", "w", encoding="UTF-8") as f:
        f.write(API)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {_APIClassName}.java FILE")


def createJavaFILE_USECASE_PARAM(e_name, useCaseFolderName, useCaseParamClassName):
    """
    Enter:
        name of entity, the name of use case & name of use case PARAM NAME
    Creates:
        useCaseParam.java File
    """
    USE_CASE_PARAM = _template_use_case_param[:]
    USE_CASE_PARAM = USE_CASE_PARAM.replace('<ENTITY>', e_name)
    USE_CASE_PARAM = USE_CASE_PARAM.replace('<USECASEFOLDER>', useCaseFolderName)

    #SAVE USE CASE PARAM
    with open(f"output/{e_name}/getAll{e_name}UseCase/{useCaseParamClassName}.java", "w", encoding="UTF-8") as f:
        f.write(USE_CASE_PARAM)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {useCaseParamClassName}.java FILE")


def createJavaFILE_USECASE_CONTRACT(e_name, useCaseContractClassName, useCaseFolderName):
    """
    Enter:
        name of entity, name of contract class and the name of use case folder
    Creates:
        useCaseContract.java File
    """
    USE_CASE_CONTRACT = _template_use_case_contract[:]
    USE_CASE_CONTRACT = USE_CASE_CONTRACT.replace('<ENTITY>', e_name)
    USE_CASE_CONTRACT = USE_CASE_CONTRACT.replace('<USECASEFOLDER>', useCaseFolderName)

    #SAVE USE CASE CONTRACT
    with open(f"output/{i}/getAll{i}UseCase/{useCaseContractClassName}.java", "w", encoding="UTF-8") as f:
        f.write(USE_CASE_CONTRACT)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {useCaseContractClassName}.java FILE")


def createJavaFILE_USECASE_IMPLEMENTATION(e_name, useCaseImplClassName, useCaseFolderName, serviceClassName, serviceVarName):
    """
    Enter:
        name of entity, name of contract class and the name of use case folder
    Creates:
        useCaseContract.java File
    """
    USE_CASE = _template_use_case_implementation[:]
    USE_CASE = USE_CASE.replace('<ENTITY>', e_name)
    USE_CASE = USE_CASE.replace('<USECASEFOLDER>', useCaseFolderName)
    USE_CASE = USE_CASE.replace('<SERVICE>', serviceClassName)
    USE_CASE = USE_CASE.replace('<service>', serviceVarName)


    #SAVE USE CASE IMPL
    with open(f"output/{e_name}/getAll{e_name}UseCase/{useCaseImplClassName}.java", "w", encoding="UTF-8") as f:
        f.write(USE_CASE)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {useCaseImplClassName}.java FILE")


def createJavaFILE_DAO_REPOSITORY(e_name, e_vars, repositoryClassName):
    """
    Enter:
        name of entity and name of repository class
    Creates:
        entityRespository.java
    """
    DAO_REPOSITORY = _template_dao_repository[:]
    DAO_REPOSITORY = DAO_REPOSITORY.replace('<ENTITY>', e_name)
    _typeID = getIDTypeToJava(e_vars)
    DAO_REPOSITORY = DAO_REPOSITORY.replace('<ID-TYPE>', _typeID)


    #SAVE DAO Repository
    with open(f"output/{i}/{i}DAO/{repositoryClassName}.java", "w", encoding="UTF-8") as f:
        f.write(DAO_REPOSITORY)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {repositoryClassName}.java FILE")


def createJavaFILE_DAO_SERVICE(e_name, serviceClassName, repositoryClassName):
    """
    Enter:
        name of entity and name of repository class
    Creates:
        entityRespository.java
    """
    DAO_SERVICE = _template_dao_service[:]
    DAO_SERVICE = DAO_SERVICE.replace('<ENTITY>', e_name)
    DAO_SERVICE = DAO_SERVICE.replace('<REPOSITORY>', repositoryClassName)
    _daoRepositoryVarName = repositoryClassName.lower()
    DAO_SERVICE = DAO_SERVICE.replace('<repository>', _daoRepositoryVarName)


    #SAVE DAO Service
    with open(f"output/{i}/{i}DAO/{serviceClassName}.java", "w", encoding="UTF-8") as f:
        f.write(DAO_SERVICE)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {serviceClassName}.java FILE")


def createJavaFILE_DAO_ENTITY(DAO_class_name, e_name, DAO_e_vars):
    """
    Enter:
        name of DAO class, name of entity and all vars of DAO entity.
    Creates:
        entityDAO.java
    """
    DAO_ENTITY = _template_dao_entiry[:]
    DAO_ENTITY = DAO_ENTITY.replace('<ENTITY>', e_name)
    DAO_ENTITY = DAO_ENTITY.replace('<VARS>', DAO_e_vars)

    #SAVE DAO Entity
    with open(f"output/{e_name}/{e_name}DAO/{DAO_class_name}.java", "w", encoding="UTF-8") as f:
        f.write(DAO_ENTITY)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {DAO_class_name}.java FILE")


def createJavaFILE_MAPPER(mapperClassName, e_name, e_vars):
    """
    Enter:
        name of class mapper, name of entity and list of vars
    Creates:
        EntityMapper.java
    """
    MAPPER_ENTITY = _template_mapper_entiry[:]
    MAPPER_ENTITY = MAPPER_ENTITY.replace('<ENTITY>', e_name)
    _toJPAEntity = getJavaMapperToJPAEntity(e_name, e_vars)
    MAPPER_ENTITY = MAPPER_ENTITY.replace('<TO-JPA-ENTITY>', _toJPAEntity)
    _toDomainEntity = getJavaMapperToDomainEntity(e_name, e_vars)
    MAPPER_ENTITY = MAPPER_ENTITY.replace('<TO-DOAMIN-ENTITY>', _toDomainEntity)

    #SAVE MAPPER
    with open(f"output/{e_name}/{mapperClassName}.java", "w", encoding="UTF-8") as f:
        f.write(MAPPER_ENTITY)
        saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A {mapperClassName}.java FILE")


#SAVE FILES
for i in _DATA: 
    createFolderEntity(i)
    createFolderGetAllEntityUseCase(i)
    createFolderEntityDAO(i)
    # Names of Class And Objects
    _entity = i
    _useCaseFolderName = f"getAll{i}UseCase"
    _useCaseName = _useCaseFolderName[0].upper() + _useCaseFolderName[1:]
    _useCaseParamName = f"GetAll{i}UseCaseParam"
    _useCaseContractName = f"GetAll{i}UseCase"
    _useCaseVarName = _useCaseName.lower()
    _useCaseImplClassName = f"GetAll{i}UseCaseImpl"
    _useCaseServiceName = f"{i}Service"
    _useCaseServiceVarName = _useCaseServiceName.lower()
    _daoRepositoryClassName = f"{i}Repository"
    _daoServiceClassName = f"{i}Service"
    _daoEntityClassName = f"{i}Entity"
    _mapperClassName = f"{i}Mapper"
    _vars = getAllAttribsToJava(_DATA[i])
    _varsEntity = getAllAttribsToJPA(_DATA[i])

    # TEMPLATES.JAVA
    createJavaFILE_ENTITY(_entity, _vars)
    createJavaFILE_API(_entity, _useCaseFolderName, _useCaseName, _useCaseVarName, _useCaseParamName)
    createJavaFILE_USECASE_PARAM(_entity, _useCaseFolderName, _useCaseParamName)
    createJavaFILE_USECASE_CONTRACT(_entity, _useCaseContractName, _useCaseFolderName)
    createJavaFILE_USECASE_IMPLEMENTATION(_entity, _useCaseImplClassName, _useCaseFolderName, _useCaseServiceName, _useCaseServiceVarName)
    createJavaFILE_DAO_REPOSITORY(_entity, _vars, _daoRepositoryClassName)
    createJavaFILE_DAO_SERVICE(_entity, _daoServiceClassName, _daoRepositoryClassName)
    createJavaFILE_DAO_ENTITY(_daoEntityClassName, _entity, _varsEntity)
    createJavaFILE_MAPPER(_mapperClassName, _entity, _vars)
    # END FOR


# SAVE SQL FILE
with open("output/sql.sql", "w", encoding="UTF-8") as f:
    f.write(formatDataToSQL())
    saveLOG("SAVE:FILE", getDateYYYYMMDD(), getHourHHMM(), f"SAVE A sql.sql FILE")


# SAVE LOGS
_existsPreviuosLogFile = False
try:
    if os.path.isfile("log.log"):
        _existsPreviuosLogFile = True
except:
    _existsPreviuosLogFile = False

if _existsPreviuosLogFile:
    previous_log_data = ""
    with open("log.log", "r", encoding="UTF-8") as f:
        previous_log_data = f.read()
    _LOGS_ = previous_log_data + "\n" + _LOGS_

with open("log.log", "w", encoding="UTF-8") as f:
    f.write(_LOGS_)
