#Functions with outputs:

# def format_name(f_name, l_name):
#   formatted_f_name = (f_name.title())
#   formatted_l_name = (l_name.title())

#   print(f'{formatted_f_name} {formatted_l_name}')

# format_name('NOAH', "jenkIns")

def format_name(f_name, l_name):
  formatted_f_name = (f_name.title())
  formatted_l_name = (l_name.title())

  return(f'{formatted_f_name} {formatted_l_name}')
#The return marks the end of the function, so any code after a return statement won't be executed.

formated_string = format_name('NOAH', "jenkIns")
print(formated_string)

#Return explained:

# when you want candy from the vending machine, what do you need? the inputs to the vending machine "function" are money and the code for the item you want. the output of the vending machine "function" is the candy, which you then eat.
# so the vending machine "function" RETURNS candy. to you, the customer, the vending machine "function" is a black box: you don't care how the machine retrieves the item, all you care about is getting the correct item.
# now imagine that it's your job to build the vending machine. it's not a black box anymore. as the designer of the machine, you must build it so that when the money and the code are entered, the mechanism inside gets and spits out the candy. you are in charge of making sure the machine RETURNS the item correctly.
# when you write a function, you are in charge of making sure the function returns what the caller is expecting. the caller could be another function! in the vending machine case, the caller was the customer. if the customer wants a Snickers, then a Bag of Pretzels won't work. similarly, if the caller is another function, and it's expecting an Integer, then a String won't work.
# we typically use return to link functions together based on the result of a computation. the data type of that result is often important.
# not everything needs to be printed to the screen. often your program will have several functions exchanging values with each other before anything is printed out.

