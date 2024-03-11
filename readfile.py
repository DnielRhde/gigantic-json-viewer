import ijson
from pprint import pprint
import ujson
import sys

import time


def dumptofile(item,exportfile):
    #ujson.dump(item, exportfile)
    #ujson.dump(item,exportfile)

    print(ujson.dumps(item),file=exportfile)
    #ujson.dump("<COMMAHERE>",exportfile)
    # dumptofile(item,exportfile)
    #ujson.dump(item, exportfile)

tree = {}

path = ""
command = ""

def formatAndPrint(x):
    if(x[2] != None):
        if (x[1] == "map_key"):
            print(x[2] + " " + "[ ... ]")
        if (x[1] == "start_map"):
            print(x[2] + " " + "{ ... }")

#data/DAR_Totaludtraek_HF_20240306110705/DAR_Totaludtraek_HF_20240306110705.json
while(True):


    with open('data/DAR_Totaludtraek_HF_20240306110705/DAR_Totaludtraek_HF_20240306110705.json', 'r', encoding="UTF-8") as file:
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

        else:
            print("Please enter valid command")
            continue
        if(path[len(path)-4:] == "item"):
            parser = ijson.items(file,path)
            if(command == "export"):
                with open('exporteddata/'+path.split(".")[-2]+'.csv','a') as exportfile:
                    exportfile.truncate(0)
                    tempcount = 0
                    objcount = 0
                    for item in parser:
                        objcount+=1

                        if (objcount%30000 == 0):
                            print("≈ "+str(objcount)+" objects exported to file...",end="\r")

                        print(ujson.dumps(item),file=exportfile)


                    print("Out of parser")

            if(command == "go"):
                objectCounter = 5
                for item in parser:
                    objectCounter-=1
                    if(objectCounter < 0):
                        break
                    pprint(item)
                    print("")


        else:
            i = ijson.parse(file)
            if(path==""):
                [formatAndPrint(x) for x in i if x[0]==""]
            else:
                for prefix, event, value in i:

                    prefixsplit = prefix.split(".")
                    if (path in prefixsplit and len(prefixsplit) == len(prefixsplit) + 1):
                        formatAndPrint(prefix, event,value)

        print("Process took %s seconds to finish" % (time.time() - start_time))
