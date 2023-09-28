#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv") 

# nato_dict = nato_dataframe.set_index("letter")["code"].to_dict()
# print(nato_dict)

dictionary = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}
# print(dictionary)


phrase = input("What do you need translated: \n").upper()
translation = [dictionary[letter] for letter in phrase]
print(translation)