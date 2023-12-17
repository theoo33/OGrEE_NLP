import re, json, sys
from items.Room import Room
from items.Rack import Rack

######################################## Methods to place an object next to a sibling ###################################################
def get_line_coeff(p1,p2):
    """ return a and b for an equation ax+b = y knowing two solutions of the equation"""
    if p1[0] == p2[0] and p1[1] == p2[1]:
        raise ValueError("Same point given two times")
    else:
        if p1[0] == p2[0]:
            return 'vertical line'
        else:
            return (float((p2[1]-p1[1])/(p2[0]-p1[0])) , float((p1[1]*p2[0]-p1[0]*p2[1])/(p2[0]-p1[0])))




        
if __name__ == "main":
    # print(name_to_object("/P/BASIC/A/R1/A01",'DEMO.BASIC.ocli'))
    #path = 'C:\\Users\\lemoi\\Documents\\Cours\\Commande_Entreprise\\GitHub\\OGrEE_NLP\\items\\schneider-ns1000n.json'
    path = 'C:\\Users\\lemoi\\Documents\\Cours\\Commande_Entreprise\\GitHub\\OGrEE_NLP\\items\\2crsi-dryzone-debug.json'

    struct = {}

    with open(path, encoding = 'utf-8') as json_file:

        try:
            # print(json_file.read())
            template = json.load(json_file)  # 👈️ parse the JSON with load()
            print(template)
            size = template['sizeWDHmm']
            print(size)
        except BaseException as e:
            print('The file contains invalid JSON')
            print(e)

    room = Room.create_from_template('AAA',[0,0,0],[0,90,0],path)
    print(room)




### OLD #############################################################################################################################
# def find_commands(file_name):
#     file = open(file_name, "r")
#     text = file.read()
#     pattern = re.compile(r'^[+.].*', re.MULTILINE)
#     return pattern.findall(text)
# print(find_commands('DEMO.BASIC.ocli'))


# def name_to_object(name : str, file_name : str):
#     text = open(file_name,'r').read()
#     pattern = re.compile(fr'.*{re.escape(name)}.*', flags=re.MULTILINE)
#     commands_with_object = pattern.findall(text)
#     for command in commands_with_object :
#         print(command)
#         if(re.search(r'^[+].*',command)):
#             obj,params = re.split(":",command)
#             if(re.search("bd",obj) or re.search("building",obj)):
#                 name,pos,rot,size = re.split("@",params)
#                 pos = re.split(",",pos.replace("[","").replace("]",""))
#                 size = re.split(",",size.replace("[","").replace("]",""))
#                 return ['Building',name,[float(coord) for coord in pos],float(rot),[float(dim) for dim in size]]
#             if(re.search("tn",obj) or re.search("tenant",obj)):
#                 name,color = re.split("@",params)
#                 return ['Tenant',name,color]
#             if(re.search("si",obj) or re.search("site",obj)):
#                 return ['Site',name]
#             if(re.search("ro",obj) or re.search("room",obj)):
#                 params = re.split("@",params)
#                 pos = re.split(",",params[1].replace("[","").replace("]",""))
#                 size = re.split(",",params[3].replace("[","").replace("]",""))
#                 if(len(params)==6):
#                     return ['Room',name,[float(coord) for coord in pos],float(rot),[float(dim) for dim in size],params[4],params[5]]
#                 else : 
#                     return ['Room',name,[float(coord) for coord in pos],float(params[2]),[float(dim) for dim in size],params[4]]
#             if(re.search("rk",obj) or re.search("rack",obj)):
#                 name,pos,unit,rot,size = re.split("@",params)
#                 pos = re.split(",",pos.replace("[","").replace("]",""))
#                 rot = convert_to_angles(rot)
#                 size = re.split(",",size.replace("[","").replace("]",""))
#                 return ['Rack',name,[float(coord) for coord in pos],unit,rot,[float(dim) for dim in size]]

# def convert_to_angles(rot : str):
#     if(not re.findall("\d", rot)):
#         """
#         "front": [0, 0, 180]
#         "rear": [0, 0, 0]
#         "left": [0, 90, 0]
#         "right": [0, -90, 0]
#         "top": [90, 0, 0]
#         "bottom": [-90, 0, 0]
#         """
#         match rot:
#             case "front":
#                 return [0,0,180]
#             case "rear":
#                 return [0, 0, 0]
#             case "left": 
#                 return [0, 90, 0]
#             case "right": 
#                 return [0, -90, 0]
#             case "top": 
#                 return [90, 0, 0]
#             case "bottom": 
#                 return [-90, 0, 0]
#     else :
#         return [float(angle) for angle in re.split(",",rot.replace("[","").replace("]",""))]
