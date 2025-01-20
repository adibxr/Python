import random
import string

def password_generator():
    length = int(input("Enter the password length: "))
    include_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_digits = input("Include digits? (yes/no): ").lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"

    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

password_generator()
