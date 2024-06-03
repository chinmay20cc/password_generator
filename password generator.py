import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Ensuring the password has at least one lowercase, one uppercase, one digit, and one special character
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Filling the rest of the password length with random choices from all character sets
    password_chars += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4)
    
    # Shuffling to make the password unpredictable
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def generate_passwords(length, count):
    return [generate_password(length) for _ in range(count)]

def main():
    print("Password Generator")
    print("------------------")
    length = int(input("Enter the length of the password: "))
    count = int(input("Enter the number of passwords to generate: "))
    
    try:
        passwords = generate_passwords(length, count)
        print("\nGenerated Passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}: {pwd}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
