# PYTHON READING FILES :

# file_path = "write.txt"

# with open(file_path, "r") as file :
#     content = file.read()
#     print(content)



# JSON file :
# import json

# file_path = "write_drivers.json"

# with open(file_path, "r") as file :
#     content = json.load(file)
#     print(content)
#     print(content["Lewis Hamilton"]) 



# CSV file :
import csv

file_path = "write_friends.csv"

with open(file_path, "r") as file :
    content = csv.reader(file)
    for line in content:
        print(line)
        print(line[1])


