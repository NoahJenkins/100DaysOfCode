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

print(logo)

def grab_data():
    random_subject = random.choice(data)
    name = random_subject['name']
    follower = random_subject['follower_count']
    descriptuon = random_subject['description']
    country = random_subject['country']
    return name, follower, descriptuon, country

subject_A = grab_data()
subject_B = grab_data()
subject_A_Value = subject_A[1]
subject_B_Value = subject_B[1]

if subject_A[0] == subject_B [0]:
    subject_B = grab_data()
# print(f'{subject_B[0]}')

subject_A_Value = subject_A[1]
subject_B_Value = subject_B[1]

print(f'Compare A: {subject_A[0]}, a {subject_A[2]}, from {subject_A[3]}')
print(subject_A_Value)

print(vs)

print(f'Compare B: {subject_B[0]}, a {subject_B[2]}, from {subject_B[3]}')
print(subject_B_Value)

def compare(subject_A, subject_B):
    
    if subject_A > subject_B:
        answer = subject_A
    else:
        answer = subject_B
    question = input('Who do you think has a higher follower count? A or B: ').lower
    if answer == question:
        return 1
    else:
        return 0

score = 0

score += int(compare(subject_A, subject_B))
print(score)


