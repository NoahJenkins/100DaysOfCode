import random
from art import logo
from art import vs
from game_data import data

#break down problems

#print logo
#The following code would need to be in a while loop. 
#print random data as compare A
#Print VS
#Print random data as compare B
#Ask user to choose a or b
#IF user is correct, add 1 life. 
#Correct answer now becomea A
#If user is wrong, game ends. 

# first_entry = data[0]
# name = first_entry['name']
# follower_count = first_entry['follower_count']
# description = first_entry['description']
# country = first_entry['country']


def grab_data():
    random_subject = random.choice(data)
    name = random_subject['name']
    follower = random_subject['follower_count']
    descriptuon = random_subject['description']
    country = random_subject['country']
    return name, follower, descriptuon, country

subject_A = grab_data()
subject_B = grab_data()
print(subject_A)
print(subject_B)

