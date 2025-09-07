#                                        super()  :

# Function used in a child class to call methodsfrom superclass
# allows you to extend the functionality of the inherited methods




class Shapes():
    def __init__(self, color):
        self.color = color



class Circle(Shapes):
    def __init__(self, color, radius):
        
        super().__init__(color)
        self.radius = radius 



class Square(Shapes):
    def __init__(self, color, width):
       
       super().__init__(color)
       self.width = width




class Rectangle(Shapes):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height 
        self.width = width






circle = Circle("red", 5)
# rectangle = Rectangle("blue",34, 17)
# square = Square("yellow", 20, 20)

print(circle.color)  
print(circle.radius)   

