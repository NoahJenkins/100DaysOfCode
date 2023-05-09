# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


lover1 = name1.lower()
lover2 = name2.lower()

couple = lover1 + lover2

print(couple)


t_count = int(couple.count('t')) 
r_count = int(couple.count('r')) 
u_count = int(couple.count('u')) 
e_count = int(couple.count('e')) 

TRUE = t_count + r_count + u_count + e_count

l_count = int(couple.count('l')) 
o_count = int(couple.count('o')) 
v_count = int(couple.count('v')) 
ee_count = int(couple.count('e')) 

LOVE = l_count + o_count + v_count + ee_count

score = TRUE + LOVE

if score < 10 or score > 90:
    print(f"Your score is {score}%, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}%, you go are alright together.")
else:
    print(f'Your score is {score}.')