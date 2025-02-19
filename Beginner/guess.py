import random

lwr = int(input("Enter the lower limit: "))
upr = int(input("Enter the upper limit: "))

num = random.randint(lwr, upr)
guess = int(input(f"Guess a number in between {lwr} and {upr}: "))

while guess != num: 
    
    if guess < num: 
        print("Too low!!")
             
    elif guess > num: 
        print("Too high!")
        
    guess = int(input("Enter the number again: "))
        
print("You guessed it right!") 
        
    