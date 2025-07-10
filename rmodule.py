# using random module of python

import random

# number = random.randint(1,6)

# low = 1
# high = 100
# number = random.randint(low, high) 

# number = random.random()                        #will return a random floating number between 0 and 1
# print(number) 

# options  = ("rock", "paper", "scissor")
# option = random.choice(options)
# print(option)


cards = ["1", "2", "3", "4","5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]

random.shuffle(cards)
print(cards)