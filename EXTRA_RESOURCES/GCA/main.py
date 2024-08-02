"""
                                FelipedelosH
                                    2024

    :WARNING: DONT EXECUTE THIS SCRIPT IN SPRINGBOOT PROJECT ROOT :WARNING:

SQL code generator
Spring boot Code Generator
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
_template_sql = loadFile("templates/sql.txt")
_template_api = loadFile("templates/getAllClassAPI.txt")
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


#SAVE FILES
for i in _DATA:
    createFolderEntity(i)
    createFolderGetAllEntityUseCase(i)
    # CREATE API
    _APIClassName = f"get{i}ApiRest"
    _useCaseFolderName = f"getAll{i}UseCase"
    _useCaseName = _useCaseFolderName[0].upper() + _useCaseFolderName[1:]
    _useCaseVarName = _useCaseName.lower()

    _entity = i


    API = _template_api[:]
    API = API.replace('<USECASEFOLDER>', _useCaseFolderName)
    API = API.replace('<ENTITY>', _entity)
    API = API.replace('<USECASE>', _useCaseName)
    API = API.replace('<USECASEPARAM>', _useCaseName+"Param")
    API = API.replace('<usecase>', _useCaseVarName)

    #SAVE
    with open(f"output/{i}/{_APIClassName}.java", "w", encoding="UTF-8") as f:
        f.write(API)

# SAVE SQL FILE
with open("output/sql.sql", "w", encoding="UTF-8") as f:
    f.write(formatDataToSQL())