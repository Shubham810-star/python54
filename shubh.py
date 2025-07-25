import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Simple Password Generator 🔐")
    
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
