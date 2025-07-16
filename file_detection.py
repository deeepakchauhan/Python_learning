# FILE      DETECTION      IN       PYTHON : 



# to work with files, we need to import the os module : 
# OS module enables us to interact with the operating system 
# Relative file path = folder/file.txt
# Absolute file path = C:/Users/deepa/desktop/file.txt




import os 

file_path = "file_detection.txt"

if os.path.exists(file_path):                     #checks whether the file exists or not , will return aboolean value 
    print(f"The location '{file_path}' exists")
else :
    print("that location doesn't exists")    

    


