import random
import string
from password_strength import check_strength

def generate_password(length,use_numbers=True,use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    characters = letters
    if use_numbers:
        characters += digits 
    if use_symbols:
        characters += symbols

    password = ''
    for i in range(length):
        password += random.choice(characters)

    return password

print("-"*50)
print("                PASSWORD GENERATOR                ")
print('-'*50)
count = int(input("How many passwords do you want to generate : "))
numbers = input("Include numbers? y/n ",).lower()
symbols = input("Include symbols? y/n ",).lower()

use_numbers = numbers == 'y'
use_symbols = symbols == 'y'

print("Generated Passwords")

for i in range(count):
    length = int(input(f"Enter length for password {i+1}: "))

    password = generate_password(length, use_numbers, use_symbols)
    strength = check_strength(password)

    print("{}  is   {}".format(password,strength))
    print()
