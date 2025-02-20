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

print("Select the operation: ")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")


while True: 
        
    choice = input("Enter your operation (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'): 
        try: 
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
                
        except ValueError: 
            print("Invalid Input!")
            continue

        if choice == '1': 
            print(f"The additon is, {add(x,y)}")
            
        if choice == '2': 
            print(f"The subtraction is, {diff(x,y)}")
            
        if choice == '3': 
            print(f"The multiplication is, {mult(x,y)}")

        if choice == '4': 
            result = div(x,y)
            if isinstance(result, str): 
                print(result)
            else: 
                print(f"The division is, {result}")
            
        again = input("Do you want to run it again? (y/n): ").lower()
        
        if again != 'y': 
            print("Thankyou for using the calculator application :)")
            break
        
    else: 
        print("Invalid Input! Enter operations from (1/2/3/4)")