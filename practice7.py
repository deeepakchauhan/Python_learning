# Concession stand program

menu = {"pizza": 2.77,
        "popcorn": 4.77,
        "burger": 3.50,
        "nachos" : 4.44,
        "fries" : 3.22,
        "chips": 5.00,
        "soda": 2.22,
        "lemonade": 2.99}

cart = []                                                              # to keep track of the users selected items
total = 0                                                              # to keep track of the total
print("----------MENU----------")                                      # decorative texts 
for key, value in menu.items():
    print(f"{key:10} : ${value : .2f}")                                # i have used format specifier here, 2f is to display two decimal places 

print("----------MENU----------")  

while True:                                                           # while , our condition will be true 
    food = input("Select an item from the menu(q to quit): ").lower()
    if food == "q":
        break 
    elif menu.get(food) is not None:
        cart.append(food)

print("----------YOUR ORDER----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total}")