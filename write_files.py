# PYTHON WRITING FILES : 
# Different modes :   
# w = to write 
# x = create a new file, and open it for writing 
# a = append new data to a file 


siblings  = ["deepak", "yuvraj", "anurag", "pooja", "aastha"]

txt_data = "My name is deepak chauhan"

file_path = "write.txt"        

# file_path = "C:\\Users\\deepa\\Desktop\\write.txt"             # relative path, also use double backslash or a forward slash                                 

with open(file_path, "a") as file :                             # first parameter = name of the file, second parameter = mode 
    # file.write( "\n" + txt_data)
    
    for sibling in siblings:                                    # working with collections 
        file.write(sibling + "\n")
        print(f"txt file '{file_path}' was created")            # write.txt file will be created with txt_data in it 


