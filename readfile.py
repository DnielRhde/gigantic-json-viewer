import ijson
from pprint import pprint
from zipfile import ZipFile
import time
import exporter

tree = {}

path = ""
command = ""

def getPathEvents(file,parentpath):
    foundbool = 0
    for x in ijson.parse(file):
        if parentpath in x[0]:
            foundbool = True
            yield x
        else:
            if foundbool == True:
                break

def formatAndPrint(x):
    if(x[2] != None):
        if (x[1] == "map_key"):
            print(x[2] + " " + "[ ... ]")
        if (x[1] == "start_map"):
            print(x[2] + " " + "{ ... }")

#data/DAR_Totaludtraek_HF_20240306110705/DAR_Totaludtraek_HF_20240306110705.json
while(True):
    with ZipFile("data/Ejendomsbeliggenhed_Simpel_HF_20240318162534.zip", 'r') as zipfile:
        #zipfile.printdir()
        with zipfile.open('Ejendomsbeliggenhed_Simpel_HF_20240318162534.json', 'r') as file:
            print("")
            print("(!) Use 'go <distination>' to view structure. Write '' in <distination> to get top-level")
            print("(!) Use 'export <distination>.item' to export the list with all its objects to ndjson")
            print("")
            command = input("command: ")
            start_time = time.time()
            if(command[:2] == "go"):
                print("")
                path = command[3:len(command)]
                command = "go"
            elif(command[:6] == "export"):
                print("")
                path = command[7:len(command)]
                command = "export"
                print(path.split(" "))
                exporter.export(file,path.split(" "))
                break
            else:
                print("Please enter valid command")
                continue
            if(path[len(path)-4:] == "item"):

                if(command == "go"):


                    parser = ijson.items(getPathEvents(file, path), path)
                    objectCounter = 5
                    for item in parser:
                        objectCounter-=1
                        if(objectCounter < 0):
                            break
                        pprint(item)
                        print("")


            else:
                if(path==""):
                    i = ijson.parse(file)
                    [formatAndPrint(x) for x in i if x[0]==""]
                else:
                    i = getPathEvents(file,path)


                    [formatAndPrint(x) for x in i if len(x[0].split(".")) == len(path.split("."))+1]
                    break
                    print("kk")
                    for x in i:
                        prefixsplit = x[0].split(".")
                        if (path in prefixsplit and len(prefixsplit) == len(path.split(".")) + 1):
                            formatAndPrint(x)


            print("Process took %s seconds to finish" % (time.time() - start_time))
