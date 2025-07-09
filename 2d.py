# creating 2D lists

# fruits = ["apple", "orange", "guava", "coconut"]
# vegetables = ["potato", "tomato", "spinach", "onion"]
# snacks = ["chips", "kurkure", "namkeen", "cold drinks"]

# groceries = [fruits, vegetables, snacks]



# print(groceries[2][2])

#using loops,
 
groceries = [["apple", "orange", "guava", "coconut"],
             ["potato", "tomato", "spinach", "onion"],
             ["chips", "kurkure", "namkeen", "cold drinks"]]

for collections in groceries:
    for food in collections:
        print(food, end=" ")

    print()        