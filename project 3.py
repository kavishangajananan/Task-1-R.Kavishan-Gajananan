# ==========================================
# ADVANCED RANDOM PASSWORD GENERATOR
# DecodeLabs - Python Project 3
# ==========================================

# Import required modules
import random
import string

# Program heading
print("======================================")
print("     ADVANCED PASSWORD GENERATOR      ")
print("======================================\n")

# Ask user for password length
length = int(input("Enter password length: "))

# Check minimum password length
if length < 4:
    print("\nPassword length should be at least 4")
else:

    # Generate one uppercase letter
    uppercase = random.choice(string.ascii_uppercase)

    # Generate one lowercase letter
    lowercase = random.choice(string.ascii_lowercase)

    # Generate one digit
    number = random.choice(string.digits)

    # Generate one special character
    symbol = random.choice(string.punctuation)

    # Combine all available characters
    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    # Remaining password length
    remaining_length = length - 4

    # Create initial password
    password = uppercase + lowercase + number + symbol

    # Add remaining random characters
    for i in range(remaining_length):
        password += random.choice(all_characters)

    # Convert password into list
    password_list = list(password)

    # Shuffle password characters
    random.shuffle(password_list)

    # Convert list back into string
    final_password = "".join(password_list)

    # Display final password
    print("\n======================================")
    print("         GENERATED PASSWORD           ")
    print("======================================")

    print("Password :", final_password)

    print("\n======================================")
    print(" PASSWORD GENERATED SUCCESSFULLY!     ")
    print("======================================")
