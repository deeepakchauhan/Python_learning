# creating a quiz game 
   
questions = (("1. Number of bones a human body has?"),
             ("2. Hottest planet in our solar system?"),
             ("3. Number of elements in the periodic table?"),
             ("4. Most abundant gas in the earth's atmosphere?"))

options = (("a. 206", "b. 207", "c. 208", "d. 209"),
           ("a. Earth", "b. Mars", "c. Mercury", "d. venus"),
           ("a. 100","b. 105", "c. 110", "d. 118"),
           ("a. hydrogen", "b. oxygen", "c. nitrogen", "d. carbon-dioxide"))

answers = ("a", "d", "d", "c")

guesses = []

question_num = 0
score = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("choose the correct answer: ").lower() 
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1 
        
        print("your answer is correct")
       
    else:
        print("your answer is incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1    


print("--------RESULTS---------") 




        
    