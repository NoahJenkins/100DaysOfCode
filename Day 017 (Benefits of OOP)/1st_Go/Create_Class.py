#Creating a class
class User:
    pass
#PascalCase for class name (first letter of each word is capitalized), it is used for classes only

#camelCase for variable name (first letter of each word is capitalized except the first word)

#snake_case for function name (all letters are lowercase and words are separated by an underscore)

#Creating an object
user_1 = User()

#Attaching attributes to an object (attributes are variables that belong to an object)
user_1.id = "001"
user_1.username = "Noah"

#Attaching attributes to an object (attributes are variables that belong to an object)

print(user_1.username)

#Creating another object
user_2 = User()
user_2.id = "002"
user_2.username = "Bob"

print(user_2.username)

#Contructors
#A constructor is a function that gets called at the creation of an object
#It is used to initialize the object's attributes
#It is defined with the __init__() method
#It is called automatically when an object is created

#Creating a class with a constructor
class User:
    def __init__(self):
        print("New user being created...")

#Creating another constructor
class Car:
    def __init__(self, seats):


# my_car = Car(5):

# #the below code would be the same as the above code if we had a constructor

# my_car.seats = 5


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "Noah")
print(user_1.id)
print(user_1.username)

# Output:
# 001
# Noah

#setting a default value for an attribute
class User:
    
        def __init__(self, user_id, username):
            self.id = user_id
            self.username = username
            self.followers = 0
            self.following = 0

#a default value can be set for an attribute in the constructor by setting it equal to a value, it cannot be set to a variable
#value vs variable
#value is a number, string, boolean, etc.
#variable is a name that represents a value