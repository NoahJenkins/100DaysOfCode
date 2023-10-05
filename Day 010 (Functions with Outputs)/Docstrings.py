#Docstrings are used to describe a function:

def format_name(f_name, l_name):
  """This takes a first and last name and formatis it to return the title case version of the
  name. Notice how this allows you to use multiple lines of code for a single text"""
  formatted_f_name = (f_name.title())
  formatted_l_name = (l_name.title())

  return(f'{formatted_f_name} {formatted_l_name}')
#The return marks the end of the function, so any code after a return statement won't be executed.

formated_string = format_name('NOAH', "jenkIns")
print(formated_string)

#Put your cursor over the function below, and the above docstring will show up, explaing what the function does. 
format_name()
