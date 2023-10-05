# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#A dictionary uses a Key Valye relationship. 

#A dictionary can be organize for readability (see below)

# Dictionary = {
# Key1: Value 1, 
# Key 2: Value 2, 
# Key 3, Value 3
# }

programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.", 
}

#Retreiving data from a dictionary

print(programming_dictionary["Bug"])

#Adding items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A new/edited definition, perhaps a moth in your computer"

#Loop through a dictionar
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])