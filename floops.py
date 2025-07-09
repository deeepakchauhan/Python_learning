# For loops = executes a block of code a fixed number of times 
#  you can iterate over a range, string, sequence , etc 

# for x in range(1,11):
#     print(x)

# for x in reversed(range(1,11)):   #to count backwards 
#     print(x)

# print("Hello, World!")

#to skip over an iteraton , use the continue keyword 

# for x in range(1,21):
#     if x==13:
#         continue
#     else:
#         print(x) 

for x in range(1,21):
    if x==13:
        break                #will nit print numbers after 12
    else:
        print(x)