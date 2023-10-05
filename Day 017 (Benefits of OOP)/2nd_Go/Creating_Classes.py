class User:
    def __init__(self, user_id, username):
        #these are all examples of attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #example of method:
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", 'Noah')
user_2 = User('002', "Jack")

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)

#Constructor
#also known as initialize, we use init function __init__()

class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode():
        self.seats = 2
my_car = Car(5)

print(my_car.seats)

#Adding Methods to classes