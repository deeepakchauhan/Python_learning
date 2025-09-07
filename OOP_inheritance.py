#                                                INHERITANCE : 

# Allows a class to inherit attributes and methods from other class
# Helps with code reusability, and extensibilty. 


class Animal : 
    def __init__(self, name):
        
        # attributes :
        self.name = name 
        self.is_alive = True 
    
    def eat(self):
        print(f"{self.name} is eating ")

    def sleep(self):
        print(f"{self.name} is sleeping")

# methods:
class Dog(Animal):
    pass 

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("Scooby")
cat = Cat("Garfeild")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
mouse.sleep()