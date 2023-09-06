#Functions with outputs:

def format_name(f_name, l_name):
  print(f_name.title())
  print(l_name.title())

format_name("noah", "JENKINS")

def format_name(f_name, l_name):
  first = f_name.title()
  last = l_name.title()
  print(f'{first} {last}')

format_name("noah", "JENKINS")

def format_name(f_name, l_name):
  first = f_name.title()
  last = l_name.title()
  return(f'{first} {last}')

formated_string=format_name("noah", "JENKINS")
print(formated_string)