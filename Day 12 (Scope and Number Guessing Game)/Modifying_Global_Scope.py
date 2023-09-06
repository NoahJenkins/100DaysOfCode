#Modifying Global Scope
#If we want to modify a global variable inside a function, we can use the global keyword.
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")
#Output:
# enemies inside function: 2
# enemies outside function: 2
#
#Global Constants
#In Python, we use CAPITAL_SNAKE_CASE to declare a constant and it is a common practice for programmers to indicate to other programmers that the variable should remain constant.
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@GeekyVoices"
#
