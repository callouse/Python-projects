import math

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def sum(x, y):
    return x + y 

def diff(x, y): 
    return x - y

def mult(x, y): 
    return x * y

def div(x, y): 
    return x/y

print(f"The addition is, {sum(x,y)}")
print(f"The subtraction is, {diff(x,y)}")
print(f"The multiplication is, {mult(x,y)}")
print(f"The division is, {div(x,y)}")
