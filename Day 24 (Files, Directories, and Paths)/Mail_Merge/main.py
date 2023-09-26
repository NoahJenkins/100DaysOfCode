#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACE_HOLDER = "[name]"

file_letters = "Day 24 (Files, Directories, and Paths)\\Mail_Merge\\Input\\Letters\\starting_letter.txt"
file_names = "Day 24 (Files, Directories, and Paths)\\Mail_Merge\\Input\\Names\\invited_names.txt"
output_folder = "Day 24 (Files, Directories, and Paths)\\Mail_Merge\\Output\\ReadyToSend"

with open(file_names) as name_files:
    #The readlines() method returns a list containing each line in the file as a list item.
    names = name_files.readlines()
    print(names)

with open(file_letters) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # The strip() method removes any leading, and trailing whitespaces.
        # Leading means at the beginning of the string, trailing means at the end.
        # You can specify which character(s) to remove, if not, any whitespaces will be removed.
        stripped_name = name.strip()
        #The replace() method replaces a specified phrase with another specified phrase.
        new_letter = letter_contents.replace(PLACE_HOLDER, stripped_name)
        print(new_letter)
        with open(f"Day 24 (Files, Directories, and Paths)\\Mail_Merge\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode ="w") as completed_letter:
            completed_letter.write(new_letter)





