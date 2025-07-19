#                                           DECORATORS : 

# A function that extends the behaviour of another function without modifying it,  
# using decoratoes means , we are adding some extra features without modifying the function
# we pass the base function as an argument to the decorator 


def add_sprinklers(func):
    def wrappers ():                              # This will wrap around the original function (like a gift wrap)
        print("add some sprinklers")
        func()                                    # This calls the original function that was passed into the decorator.
    return wrappers



@add_sprinklers
def get_ice_cream():
    print("here is your ice-cream")

get_ice_cream()    


