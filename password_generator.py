import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("Password should be at least 6 characters long.")
                continue
            return length
        except ValueError:
            print("Please enter a valid number.")

def choose_complexity():
    print("\nChoose password type:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Symbols (Recommended)")
    
    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if choice == 1:
                return string.ascii_letters
            elif choice == 2:
                return string.ascii_letters + string.digits
            elif choice == 3:
                return string.ascii_letters + string.digits + string.punctuation
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length, characters):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    
    # Get user preferences
    length = get_password_length()
    characters = choose_complexity()
    
    # Generate password
    password = generate_password(length, characters)
    
    # Display result
    print(f"\nYour password: {password}")
    print(f"Length: {length} characters")
    
    # Ask to generate another
    if input("\nGenerate another password? (y/n): ").lower() == 'y':
        main()
    else:
        print("Thanks for using Password Generator!")

# Run the program
main()