import  random

low = 1
high = 100
number = random.randint(low, high)
guesses = 0

while True:
    guess = int(input(f"enter a between {low} - {high}: "))
    guesses += 1

    if guess > number:
        print(f"{guess} is too high")
    elif guess < number :
        print(f"{guess} is too low")
    else:
        print(f"{guess} is correct")
        break 

print(f"you took {guesses} guesses")