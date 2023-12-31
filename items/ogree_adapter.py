import json


def createRoomFromTemplate(name :str, position : list, rotation : int, filename : str) -> str:
    """Creates a Room instance from a json file with a template"""
    filename = "demo/rooms/" + filename + ".json"
    with open(filename, "r") as room:
        roomDescription = json.load(room)
    r = roomDescription
    return r

def readFileOCLI(filename : str, searched : str) -> (int,str):
    """Reads an OCLI file and returns a string"""
    k = 0
    with open(filename, "r") as commands:
        line = commands.readline()
        while line and line.find(searched) == -1:
            line = commands.readline()
            k += 1
        if not line:
            raise ValueError("There is no element named {} in {}".format(searched,filename))
    return k, line

def readCommandOCLI(command : str) -> list:
    """Reads an OCLI command and converts it"""
    #a command is always separated from its paramaters by a semicolon
    parts = command.split(":")
    typeOfCommand = parts[0]
    parameters = parts[1].split("@")
    return typeOfCommand, parameters
    
def executeCommandOCLI(command : str, parameters : list):
    #return TERRORIST[command](parameters)
    pass

def terrorist(parameters : list):
    reifiedParameters = []
    for parameter in parameters:
        try:
            reifiedParameters.append(json.loads(parameter))
        except json.decoder.JSONDecodeError:
            reifiedParameters.append(parameter)
    return reifiedParameters


def createRoom(parameters : list):
    """Creates a room from given parameters"""
    if len(parameters) != 4:
        raise TypeError("An incorrect number of arguments was given")
    name = parameters[0]
    position = json.loads(parameters[1])
    rotation = json.loads(parameters[2])
    template = json.loads(parameters[3])
    return [name,position,rotation,template]

def getTypeFromName(filename : str, name : str):
    """This function is supposed to return the type of an object thanks to its name, but it might be ineffective
    in case a name is used for different objects"""
    k, line = readFileOCLI(filename, name)
    typeOfCommand, parameters = readCommandOCLI(line)
    return TYPES[typeOfCommand]


def modifyAttributesSelection(names : list, attributeName : str, attributeArgument : str) -> str:
    selection = "={" + ",".join(names) + "}" + "\n"
    return selection + "selection.{}={}".format(attributeName, attributeArgument)  
    
TYPES = []

if __name__ == "__main__":
    testCommand = "+bd:/P/BASIC/A@[0,0]@0@[24,30,1]"
    #print(readFileOCLI("demo/simu1.ocli", "/P/BASIC/A/R1"))
    #print(getTypeFromName("demo/simu1.ocli","/P/BASIC"))
    typeOfCommand, parameters = readCommandOCLI(testCommand)
    print(parameters)
    print(terrorist(parameters))
    #print(createRoom(parameters))
    #print(json.loads("[0,0]"))