import ijson
import json

pastPath = ""

while True:
    isExport = False
    path=""
    print("")
    print("(Tip:) First, to get an overview/ view toplevel objects just write '' (nothing).")
    print("(Tip:) Write the name of the object to go to.")
    print("(Tip:) Write 'back', to go 1 step back.")
    print("(Tip:) Write 'export' to export the current object or list your in, to its own file.")

    print("")
    if(pastPath == ""):
        path = pastPath + input("Command: " + pastPath)
    else:
        path = pastPath+"." + input("Command: " + pastPath + ".")
    print(path.split(".")[-1])

    #clear screen
    for room in range(30):
        print(" ")
    if(path.split(".")[-1] == "export"):
        path = ".".join(path.split(".")[:len(path.split("."))-1])
        isExport = True
        print("Exporting...")
        print("")
    elif(path.split(".")[-1] == "back"):
        print("Going back, Discovering...")
        print("")
        path = ".".join(path.split(".")[:len(path.split("."))-2])
    else:
        print("Discovering...")
        print("")
    pastPath=path




    def typeIsList(file):
        if(path==""):
            for line in file:
                for char in line:
                    if(char == "{"):
                        file.seek(0)
                        return False
                    if(char == "["):
                        file.seek(0)
                        return True
        parser = ijson.items(file, path)
        for item in parser:
            file.seek(0)
            return(type(item)==list)
        file.seek(0)
        return(False)


    def LoadItem():
        global parentElementsType
        with open('data/bbr.json', 'r',encoding="utf-8") as file:

            if(typeIsList(file)):
                parser = ijson.items(file, path+".item")
                limitCount = 3
                if (isExport):
                    with open("exporteddata/"+path.split(".")[-1]+".json", "a") as exportfile:
                        exportfile.truncate(0)
                        exportfile.write("[")
                        for item in parser:
                            exportfile.write(str(item)+",               ")
                        exportfile.write("]")
                else:
                    for item in parser:
                        if (limitCount == 0):
                            break
                        limitCount = limitCount - 1

                        print(json.dumps(str(item), indent=4, ensure_ascii=False))
            else:
                parser = ijson.kvitems(file, path)

                for item in parser:
                    if(type(item[1])==list):
                        print(str(item[0])+" [...]")
                    else:
                        print(str(item[0])+" {...}")


    LoadItem()


