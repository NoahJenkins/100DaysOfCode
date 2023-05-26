#Return Function
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#Return stops the function from running
def my_function(x):
    return 5*x
    print("Hello")
print(my_function(3))
#Return can be used to return multiple values
def my_function(x):
    return 5*x, 3*x
print(my_function(3))

###########

def format_name(f_name, l_name):
  if f_name== "" or l_name =="":
    return "You didn't provide valid inputs."
  first = f_name.title()
  last = l_name.title()
  return(f'Result: {first} {last}')

print(format_name(input("What is your first name? "), input("What is your last name? ")))