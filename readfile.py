import ijson

path = ""

#data/DAR_Totaludtraek_HF_20240306110705/DAR_Totaludtraek_HF_20240306110705.json
with open('data/DAR_Totaludtraek_HF_20240306110705/DAR_Totaludtraek_HF_20240306110705.json', 'r') as file:
    i = ijson.parse(file)
    for prefix, event, value in i:
        if not prefix or event == 'map_key' or ('.' in prefix and event in ('start_map', 'end_map') or event in ("end_map","end_array")):
            continue

        if(path in prefix.split(".") and len(prefix.split(".")) <= len(path.split("."))+1):
            print("")

            print(prefix, event, value)
        if(path=="" and len(prefix.split("."))==1):
            print("")

            print(prefix, event, value)
