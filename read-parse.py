import ijson

# Open the JSON file
with open('large_file.json', 'r') as file:
    # Parse the JSON objects one by one
    parser = ijson.items(file, 'item')

    # Iterate over the JSON objects
    for item in parser:
        # Process each JSON object as needed
        print(item)





print("test")
