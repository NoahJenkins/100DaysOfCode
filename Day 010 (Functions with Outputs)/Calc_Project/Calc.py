from art import logo 

print(logo)

#calculator

#add
def add(n1, n2):
    return n1 + n2

#substract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def mutliply(n1, n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
'+': add, 
'-': subtract, 
'*': mutliply,
'/': divide
}

#Ask for 1st number, then operation, then 2nd number

num1 = int(input('What is the first numner: '))
#Asking for 1st number

for key in operations:
    #printing operations menue
    print(key)

operation_symbol = input('Pick an operation from the line above? ')
#asking for operations

num2 = int(input('What is the seocnd numner: '))
#asking for num 2

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')