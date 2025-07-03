# to calculate radius of a circle 
import math 

radius = float(input("enter the value of radius: " ))

circumference = 2 * math.pi * radius

# print(circumference)
# using f string
print(f"the circumference of the circle is : { round(circumference , 2)}")   # will round upto 2 digits