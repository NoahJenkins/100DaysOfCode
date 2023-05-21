alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(cipher_text, shift_amount):
  message = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position + shift_amount
    elif direction == "decode":
      new_position = position - shift_amount
    message += alphabet[new_position]
  print(f"The message is: '{message}'")

ceaser(cipher_text=text, shift_amount=shift)
