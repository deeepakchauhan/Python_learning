# while loop = execute some code WHILE some condition remains true 

# age = int(input("how old are you :"))

# while age < 0:
#     print("age cannot be negative")
#     age = int(input("how old are you :"))

# print(f"You are {age} years old")    

num = int(input("enter a number between 1 to 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a number between 1 to 10: "))

print(f"your number is {num}")    