import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv") 

# nato_dict = nato_dataframe.set_index("letter")["code"].to_dict()
# print(nato_dict)

dictionary = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}
# print(dictionary)

on = True
while on:
    phrase = input("What do you need translated: \n").upper()

    try:
        translation = [dictionary[letter] for letter in phrase]
        print(translation)
        on = False

    except KeyError:
        print("Sorry, only input letters.")
