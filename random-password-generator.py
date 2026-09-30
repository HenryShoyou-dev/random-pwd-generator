import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits # If the user ask for numbers in the password, it will gen w/ numbers
    if special_characters:
        characters += special # If the user ask for special chars, it will gen w/ special chars 

    pwd = "" # Password variable for storing last password

    meets_criteria = False # A variable to check whether the password meets the criteria or not

    has_number = False
    has_special = False 

    while not meets_criteria or len(pwd) < min_length: # If the generated password doesn't meet the criteria or the length of the password isn't long enough, the while loop will run
        new_char = random.choice(characters) # Pick random char from characters variable
        pwd += new_char # Insert char from new_char to pwd variable

        if new_char in digits: 
            has_number = True # Check whether the character from new_char is a digit or not
        elif new_char in special:
            has_special = True # Check whether the character from new_char is a special character or not

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special


    return pwd # If the password has met the criteria, return the value of pwd

min_length = int(input("Enter the minimum length of your password: "))
has_numbers = input("Do you want to have numbers innit? (y/n): ") == "y"
has_special = input("Do you want to have special characters? (y/n): ") == "y"

pwd = generate_password(min_length, has_numbers, has_special)

print(pwd)