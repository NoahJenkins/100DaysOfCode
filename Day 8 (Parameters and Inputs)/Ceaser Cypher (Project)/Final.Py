import art
print(art.logo)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

game_running = True
while game_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(cipher_text, shift_amount):
        message = ""
        for char in cipher_text:
            if char.isalpha():  # Check if the character is alphabetical
                position = alphabet.index(char)
                if direction == "encode":
                    new_position = (position + shift_amount) % 26  # Wrap around if necessary
                elif direction == "decode":
                    new_position = (position - shift_amount) % 26
                char = alphabet[new_position]
            message += char
        print(f"The message {direction}d is: '{message}'")

    caesar(cipher_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        game_running = False
        print("Goodbye")
