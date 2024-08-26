from calc_art import logo
import os

# Defining functions for the different operations
def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

print(logo)

question = 'y'
number1 = int(input("Whats your first number?: "))


while question != "x":
    
    result = 0
    
    
    print("+ \n - \n * \n / \n")
    operation = input("Pick an operation: ")
    number2 = int(input("Choose another number: "))

    
    if operation == "+":
        result = add(number1, number2)
        print(f"{number1} + {number2} = {result}")
    elif operation == "-":
        result = subtract(number1, number2)
        print(f"{number1} - {number2} = {result}")
    elif operation == "*":
        result = multiply(number1, number2)
        print(f"{number1} * {number2} = {result}")
    elif operation == "/":
        result = divide(number1, number2)
        print(f"{number1} / {number2}  = {result}")
    else:
        print("Not supported operation")
        break
    
    
    question = input(f"Type 'y' to continue calculating with {number1}, or type 'n' to start a new calculation or 'x' to terminate ")
    
    if question == 'y':
        number1 = result
    elif question == 'n':
        os.system('cls')
        number1 = int(input("Whats your first number?: "))
    else:
        break
        
    
        
    
    