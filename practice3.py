# Compound interest calculator 

principle = 0
rate = 0
time = 0

while True:
    principle = float(input(" enter the principle amount: "))
    if principle < 0 :
        print("Principle amount cannot be negative")
    else:
        break    

while True:
    rate = float(input(" enter the interest rate: "))   
    if rate < 0 :
        print(" interest rate cannot be negative")
    else:
        break    

while True:
    time = float(input(" enter the given time in years: "))    
    if time < 0 :
        print("time cannot be less than zero")
    else :
        break    



total = principle * pow((1 + rate/100), time)     
print (f"balance after {time} year/s: ${total}")   

