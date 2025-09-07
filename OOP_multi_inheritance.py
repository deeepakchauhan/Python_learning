# MULTIPLE INHERITANCE :
# The derived class inherits from more than one class


# MULTILEVEL INHERITANCE :
# the derived class inherits from a parent which inherits from another parent


class Animal():
    def __init__(self, name):
        self.name = name 

        
    def eat(self):
        print(f"{self.name} can eat")




class Prey(Animal):
    def flee(self):
         
        print(f"{self.name} can flee")

class Predator(Animal):
    def hunt(self):
        
        print(f"{self.name} can hunt")
    



class Rabbit(Prey):
    pass 

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass



rabbit = Rabbit("jojo")
hawk = Hawk("Bugs")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.eat()