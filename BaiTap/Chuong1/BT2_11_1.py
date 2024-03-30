def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
file_path = "input.txt"
shift = 3

# Encrypt the file
with open(file_path, 'r') as file:
    plaintext = file.read()
encrypted_text = caesar_encrypt(plaintext, shift)

# Save the encrypted text to a new file
encrypted_file_path = "output1encrypted.txt"
with open(encrypted_file_path, 'w') as file:
    file.write(encrypted_text)

# Decrypt the file
with open(encrypted_file_path, 'r') as file:
    encrypted_text = file.read()
decrypted_text = caesar_decrypt(encrypted_text, shift)

# Save the decrypted text to a new file
decrypted_file_path = "output1decrypted.txt"
with open(decrypted_file_path, 'w') as file:
    file.write(decrypted_text)