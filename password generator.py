# Task-3 Password Generator
import secrets
import string

def generate_password(password_len):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    selection_list = letters + digits + special_chars
    password = ''
    for i in range(password_len):
        password += ''.join(secrets.choice(selection_list))
    return password

password_len = int(input("Enter the length of the password: "))
print("Generated Password : ", generate_password(password_len))
