#adding meothods to a class

class Car:
    def enter_race_mode(self):
        self.seats = 2


my_car = Car()

my_car.enter_race_mode()

print(my_car.seats)

# Output:
# 2

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Noah")
user_2 = User("002", "Bob")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Output:
# 0
# 1
# 1
# 0