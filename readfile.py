import ijson
import json

pastPath = ""

while True:
    print("")
    path=""
    if(pastPath == ""):
        path = pastPath + input("Path: " + pastPath)
    else:
        path = pastPath+"." + input("Path: " + pastPath + ".")
    print(path.split(".")[-1])
    if(path.split(".")[-1] == "back"):
        path = ".".join(path.split(".")[:len(path.split("."))-2])
    pastPath=path

    #clear screen
    for room in range(30):
        print(" ")

    print ("Discovering...")
    print("")
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
        with open('handelsoplysning.json', 'r',encoding="utf-8") as file:
            if(typeIsList(file)):
                parser = ijson.items(file, path+".item")
                limitCount = 3
                for item in parser:
                    if(limitCount==0):
                        break
                    limitCount=limitCount-1

                    print(json.dumps(str(item),indent=4,ensure_ascii=False))
            else:
                parser = ijson.kvitems(file, path)

                for item in parser:
                    if(type(item[1])==list):
                        print(str(item[0])+" [...]")
                    else:
                        print(str(item[0])+" {...}")


    LoadItem()


