import string
import random

def generate_password(length):
    """Generates a random password of the given length."""
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    all_characters = s1 + s2 + s3 + s4
    if length > len(all_characters):
        length = len(all_characters)
    return ''.join(random.choices(all_characters, k=length))

def main():
    print("\n🎉 Welcome to the Password Generator! 🎉")
    print("Create a secure and random password with just a few clicks.\n")
    
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length <= 0:
                raise ValueError("The length must be a positive number.")
            break
        except ValueError as e:
            print(f"🚫 Invalid input: {e}. Please try again.")
    password = generate_password(length)
    print("\n🔑 Your generated password is:")
    print(f"🌟 {password} 🌟\n")
    
    print("Thank you for using the Password Generator! Stay secure!")

if __name__ == "__main__":
    main()
