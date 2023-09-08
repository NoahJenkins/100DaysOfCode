import random

word_list = ["aardvark", "baboon", "camel"]

word_choice = random.choice(word_list)

print(f"Psst, the answer is {word_choice}")


guess = input('Guess a letter? ').lower()

for letter in word_choice:
    if letter == guess:
        print('right')
    else:
        print('wrong')

