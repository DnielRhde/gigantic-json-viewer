import ujson
import ijson
import time

def getPathEvents(parser,parentpath):
    start_time = time.time()

    for x in parser:
        if parentpath == x[0]:
            break


    print("Ran to path location in %s seconds" % (time.time() - start_time))
    start_time = time.time()
    foundbool = False
    for x in parser:

        if parentpath in x[0]:
            foundbool = True
            yield x
        else:
            if foundbool == True:
                break
    print("Events took %s seconds" % (time.time() - start_time))



def getPath(parser,parentpath,outputpath):

    if outputpath == None:
        outputpath = parentpath+".json"
    open('exporteddata/'+outputpath, 'w').close()
    with open('exporteddata/'+outputpath, 'a') as outputfile:

        objcount = 0
        #print("[", file=outputfile)
        for item in ijson.items(getPathEvents(parser, parentpath),parentpath+".item"):
            print(ujson.dumps(item), file=outputfile)
            objcount += 1
            if (objcount % 10000 == 0):
                print("≈ " + str(objcount) + " objects exported to file...", end="\r")

                # print("Process took %s seconds" % (time.time() - start_time))
        #print("[", file=outputfile)
        print("≈ " + str(objcount) + " objects exported to file...", end="\r")





def export(file,paths):
    parser = ijson.parse(file)
    start_time = time.time()
    print("Paths to export: ",paths)
    for path in paths:
        print("Exporting "+path)
        getPath(parser,path,None)
    print("Process took %s seconds" % (time.time() - start_time))




