# PYTHON WRITING FILES (.json):
# A JSON file is a collection of key value pairs. 



import json

drivers = {
    "Lewis Hamilton" : "Scuderia Ferrari",
    "Max Verstappen" : "Mercedes",
    "Carlos Sainz" : "Williams",
    "Oscar Piastri" : "McLaren",
    "Daniel Ricciardo" : "Red Bull Racing"
}

file_path = "write_drivers.json"

with open(file_path, "w") as file :
    json.dump(drivers, file, indent=4)                               # dump method will convert the drivers dictionary into a json string

    print(f"json file '{file_path}' was created") 