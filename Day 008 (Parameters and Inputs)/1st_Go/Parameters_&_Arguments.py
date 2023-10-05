# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello")
  print("Happy Friday!")
  print("The weather is fine today.")

greet()

def greet_with_name(name):
  print(f"Hello {name}.")
  print(f"How is are you today {name}?")

#arguement = "Noah"
#parameter = name

greet_with_name("Noah")

def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

greet_with("Noah", "New York")
# greet_with(location="New York", name="Noah") # Keyword Arguments
