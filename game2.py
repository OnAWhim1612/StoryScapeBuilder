import string

def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = (ord(char.lower()) - ord('a') + shift) % 26
            encrypted_char = chr(ord('A' if is_upper else 'a') + char_index)
            encrypted_text += encrypted_char.upper() if is_upper else encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

# Example usage:
shift_value = 3
plaintext = "HELLO WORLD"
encrypted_message = caesar_encrypt(plaintext, shift_value)

print(f"Encrypted Message: {encrypted_message}")
# Display the encrypted image here (you can use libraries like PIL to generate images).

# For the player input:
player_input = input("Enter your decoded message: ").upper()
decrypted_message = caesar_decrypt(encrypted_message, shift_value)

if player_input == decrypted_message:
    print("Correct! You cracked the code!")
else:
    print("Sorry, try again!")

