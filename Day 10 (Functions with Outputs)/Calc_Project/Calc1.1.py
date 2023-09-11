from art import logo 

print(logo)

#calculator

#Add 
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
  for key in operations.keys():
      print(key)
  
  num1 = float(input("What's the first number?: "))
  
  thinking = True
  
  while thinking == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
  
    if operation_symbol in operations:
        operation_func = operations[operation_symbol]
        answer = operation_func(num1, num2)
      
    print(f'{num1} {operation_symbol} {num2} = {answer}')
      
    choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a fresh calculation: ").lower()
  
    if choice == 'y':
        num1 = answer
    else:
        thinking = False
        calculator()
# recursion
#Recursion is when a function calls itself.


calculator()
