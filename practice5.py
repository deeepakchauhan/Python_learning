# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("enter the name of the food to buy (q to quit): ")
    if food == "q":
        break  
    else :
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")        

for food in foods:
    print(food, end=" ")

print()

for price in prices:
    print(price, end=" ")
