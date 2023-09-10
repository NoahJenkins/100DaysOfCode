# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.

# You've been to Moscow and Saint Petersburg.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.

# Hint
# Look at the function call above to see what the name of the function should be.

# The inputs for the function are positional arguments. The order is very important.

# Feel free to choose your own parameter names.

# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, cities):
    new_country = {
    "country": "Russia",
    "Visits": 2,
    "cities": ["Moscow", "Saint Petersburg"]
    }
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)