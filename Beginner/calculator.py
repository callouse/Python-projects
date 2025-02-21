import math
import datetime

history = []

def log_history(entry): 
    history.append(entry)
    
time = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    
def add(x, y):
    return x + y 

def diff(x, y): 
    return x - y

def mult(x, y): 
    return x * y

def div(x, y): 
    if y == 0: 
        return "Error: Cannot divide by zero!"
    return x/y

def power(x, y):
    return x**y

def mod(x, y):
    return x % y; 

def root(x): 
     if x < 0: 
         return "Error: Square root only works for positive numbers!"
     return math.sqrt(x) 
 
def fact(x):
    if x < 0 or not x.is_integer(): 
        return "Error: Factorial only works for non-negetive integers!"
    return math.factorial(int(x))

print("Select the operation: ")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. EXPONENTIATION")
print("6. MODULUS")
print("7. SQUARE ROOT")
print("8. FACTORIAL")
print("9. BREAK")


while True: 
        
    choice = input("Enter your operation (1-9): ")
    
    if choice in ('1', '2', '3', '4', '5', '6'): 
        try: 
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
                
        except ValueError: 
            print("Invalid Input!")
            continue
        
        if choice == '1':
            result = add(x,y)
            log_history(f"{x} + {y} = {result}")
            print(f"The additon is, {add(x,y)}")
            
        if choice == '2': 
            result = diff(x,y)
            log_history(f"{x} - {y} = {result}")
            print(f"The subtraction is, {diff(x,y)}")
            
        if choice == '3': 
            result = mult(x,y)
            log_history(f"{x} x {y} = {result}")
            print(f"The multiplication is, {mult(x,y)}")

        if choice == '4': 
            result = div(x,y)
            if isinstance(result, str): 
                print(result)
            else: 
                log_history(f"{x} / {y} = {result}")
                print(f"The division is, {result}")
            
        if choice == '5': 
            result = power(x,y)
            log_history(f"{x} ** {y} = {result}")
            print(f"The exponent of {y} on {x} is, {power(x,y)}")
            
        if choice == '6': 
            result = mod(x,y)
            log_history(f"{x} % {y} = {result}")
            print(f"The modolus is, {mod(x,y)}")
            
    elif choice == '9': 
        print("Thankyou for you time!!")
        break
        
    elif choice in ('7', '8'): 
        try: 
            x = float(input("Enter your number: "))
            
        except ValueError: 
            print("Invalid Input")
            continue
        
        if choice == '7':
            result = root(x)
            if isinstance(result, str): 
                print(result)
            else:          
                log_history(f"sqrt of {x} = {result}")
                print(f"The square root of {x} is, {result}")
        
        if choice == '8': 
            result = fact(x)
            if isinstance(result, str): 
                print(result)
            else: 
                log_history(f"{x}! = {result}")
                print(f"The factorial of {x} is, {result}")
     
    view = input("Do you want to view history? (y/n)").lower()
    if view == 'y': 
        for entry in history: 
            print(entry)
            
    again = input("Do you want to run it again? (y/n): ").lower()        
    if again != 'y': 
        print("Thankyou for using the calculator application :)")
        break    
    
    else: 
        print("Invalid Input! Enter operations from (1-9)")
    
    # view = input("Do you want to view history? (y/n)").lower()
    # if view == 'y': 
    #     for entry in history: 
    #         print(entry)
            
    # again = input("Do you want to run it again? (y/n): ").lower()        
    # if again != 'y': 
    #     print("Thankyou for using the calculator application :)")
    #     break       
    
with open("calc_history.txt", "a") as file:
    if history:  
        file.write("Session Time: " + time + "\n\n")
        for entry in history: 
            file.write(entry + "\n")
            
        print("History stored on the text file sucessfully!")
        
    else: 
        print("No history to store")