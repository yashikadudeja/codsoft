# import string
# import random

# if __name__ == "__main__":
#     s1 = string.ascii_lowercase
#     # print(s1)
#     s2 = string.ascii_uppercase
#     # print(s2)
#     s3 = string.digits
#     # print(s3)
#     s4 = string.punctuation
#     # print(s4)
#     plen = int(input("Enter password length\n")) #Todo1: Handle Gibberish
#     s = []
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#     # print(s)
#     # random.shuffle(s)
#     # print(s)
#     print("Your password is: ")
#     print("".join(random.sample(s, plen)))
#     # print("".join(s[0:plen]))



# import string
# import random
# import sys

# def print_colored(text, color_code):
#     """Prints text in the given color."""
#     print(f"\033[{color_code}m{text}\033[0m")

# def main():
#     # Define color codes
#     BLUE = '34'
#     GREEN = '32'
#     YELLOW = '33'
    
#     # Display a welcome message
#     print_colored("Welcome to the Password Generator!", BLUE)
#     print_colored("Let's create a secure and random password for you.", GREEN)
    
#     # Get password length from user with validation
#     while True:
#         try:
#             plen = int(input("Enter the desired password length (must be a number): "))
#             if plen <= 0:
#                 raise ValueError("The length must be a positive number.")
#             break
#         except ValueError as e:
#             print_colored(f"Invalid input: {e}", YELLOW)
    
#     # Define character sets
#     s1 = string.ascii_lowercase
#     s2 = string.ascii_uppercase
#     s3 = string.digits
#     s4 = string.punctuation
    
#     # Combine all character sets
#     s = list(s1 + s2 + s3 + s4)
    
#     # Ensure the length of the password doesn't exceed the number of available characters
#     if plen > len(s):
#         plen = len(s)
#         print_colored(f"Password length adjusted to maximum available length: {plen}", YELLOW)
    
#     # Generate the password
#     password = "".join(random.sample(s, plen))
    
#     # Display the password
#     print_colored("\nYour generated password is:", BLUE)
#     print_colored(password, GREEN)

# if __name__ == "__main__":
#     main()

# import string
# import random

# def generate_password(length):
#     """Generates a random password of the given length."""
#     # Character sets
#     s1 = string.ascii_lowercase
#     s2 = string.ascii_uppercase
#     s3 = string.digits
#     s4 = string.punctuation
    
#     # Combine all character sets
#     all_characters = s1 + s2 + s3 + s4
    
#     # Ensure the password length is reasonable
#     if length > len(all_characters):
#         length = len(all_characters)
    
#     # Generate and return the password
#     return ''.join(random.sample(all_characters, length))

# def main():
#     print("\n🎉 Welcome to the Password Generator! 🎉")
#     print("Create a secure and random password with just a few clicks.\n")
    
#     while True:
#         try:
#             # Get password length from the user
#             length = int(input("Enter the desired password length (e.g., 12): "))
#             if length <= 0:
#                 raise ValueError("The length must be a positive number.")
#             break
#         except ValueError as e:
#             print(f"🚫 Invalid input: {e}. Please try again.")
    
#     # Generate the password
#     password = generate_password(length)
    
#     # Display the generated password
#     print("\n🔑 Your generated password is:")
#     print(f"🌟 {password} 🌟\n")
    
#     print("Thank you for using the Password Generator! Stay secure!")

# if __name__ == "__main__":
#     main()

import string
import random

def generate_password(length):
    """Generates a random password of the given length."""
    # Character sets
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    # Combine all character sets
    all_characters = s1 + s2 + s3 + s4
    
    # Ensure the password length is reasonable
    if length > len(all_characters):
        length = len(all_characters)
    
    # Generate and return the password
    return ''.join(random.choices(all_characters, k=length))

def main():
    print("\n🎉 Welcome to the Password Generator! 🎉")
    print("Create a secure and random password with just a few clicks.\n")
    
    while True:
        try:
            # Get password length from the user
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length <= 0:
                raise ValueError("The length must be a positive number.")
            break
        except ValueError as e:
            print(f"🚫 Invalid input: {e}. Please try again.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("\n🔑 Your generated password is:")
    print(f"🌟 {password} 🌟\n")
    
    print("Thank you for using the Password Generator! Stay secure!")

if __name__ == "__main__":
    main()
