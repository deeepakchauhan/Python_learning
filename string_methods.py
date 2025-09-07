#            STRING       METHODS :


name = input("Enter your name : ")
number = input("Enter you phone number : ")

result1 = len(name)
result2 = name.find("e")                   # will print the index of first occurence of the letter 
result3 = name.rfind("e")                  # will print the last occurence of the letter
result4 = name.find("z")                   # will print a neg index if letter is not present 
result5 = name.capitalize()                # will only capitalize the first letter of the string 
result6 = name.upper()                     # will capitalize all the letters of the string 
result7 = name.lower()                     # all lowercase
result8 = name.isdigit()                   # will return true/false ; true only iff string contains digits





print(result1)
print(result2)
print(result3)
print(result4) 
print(result5)
print(result6)
print(result8)





num1 = number.count("8")                 # counts number of 8 present 
print(num1)     
num2 = number.replace("8", "-")          # will replace 8 with -
print(num2)   


