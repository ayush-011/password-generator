import random
import string

try:
    length = int(input("Enter the desired password length (minimum 4): "))

    if length < 4:
        print("Password length should be at least 4 for security.")
    else:
        letters = string.ascii_letters  
        digits = string.digits          
        special_chars = '!@#$%^&*()'

        all_chars = letters + digits + special_chars

        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(special_chars)
        ]

        password += random.choices(all_chars, k=length - 3)
        random.shuffle(password)
        print("Generated Password:", "".join(password))

except ValueError:
    print("Please enter a valid number.")
