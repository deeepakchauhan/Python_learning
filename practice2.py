# Python calculator, by using if-else statements

operator = input("choose the operator(+,-,*,/) :")
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

# print(num1 + num2)

if operator == "+":
    result = num1+num2 
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == "*/":
    result = num1/num2
    print(result)            
else:
    print(f"{operator} is not valid")