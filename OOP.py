# OBJECT ORIENTED PROGRAMMING :

# Object = a bundle of related attributes(variables) and methods(functions).
# Class = (blueprint) used to design the structure and layout of an object.
# Methods = functions that belongs to an object. 
# class is needed to create an object. 



class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.color} {self.model}")          #self refers to the object currently we are working with

    def stop(self):
        print(f"stop the {self.color} {self.model}") 

    def describe(self):
        print(f"{self.model}  {self.color}  {self.year}")    


car1 = Car("Mercedes", 2021, "Black", False)
car2 = Car("Scuderia Ferrari", 2024, "Red", False)

# print(car1.model)  
# print(car2.model)
# print(car1.color)
# print(car2.color) 

car1.drive()    
car2.stop()
car1.describe()
car2.describe()






