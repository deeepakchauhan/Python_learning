# # PYTHON WRITING FILES (.csv):
# csv means comma seperated values ,
# they are similar to spreadsheet files

import csv

friends = [
    ["name", "surname", "age", "city"],
    ["deepak", "chauhan", 20, "panaji"],
    ["harsh", "singh", 21, "kanpur"],
    ["madhur", "sharma", 19, "jaipur"],
    
]

file_path = "write_friends.csv"


with open(file_path, "w", newline= "") as file :
    writer = csv.writer(file)
    
    for row in friends :
        writer.writerow(row)
    
    print(f"csv file '{file_path}' was created")               # writer is an object, which provides methods for a csv file