import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)  # Create a list of underscores with the same length as chosen_word
print(display)
# Testing code
print(f"Pssst, the solution is {chosen_word}.")

guess = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter



for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")



print(display)