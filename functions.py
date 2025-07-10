# functions = a block of reusable code
# place () after the function to invoke it 

# return = statement is used to end a function, and send a result back to the caller 


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("deepak", "chauhan")

print(full_name)