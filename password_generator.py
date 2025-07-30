import random
import string

def get_user_choices():
    print("==== PASSWORD GENERATOR ====")
    length = int(input("Enter the desired password length: "))
    print("Include the following in your password? (y/n)")
    use_upper = input("Uppercase letters (A-Z): ").lower() == 'y'
    use_lower = input("Lowercase letters (a-z): ").lower() == 'y'
    use_digits = input("Digits (0-9): ").lower() == 'y'
    use_special = input("Special characters (!@#$...): ").lower() == 'y'
    return length, use_upper, use_lower, use_digits, use_special

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_special:
        char_sets.append(string.punctuation)
    
    if not char_sets:
        return "Error: No character types selected!"

    # Ensure at least one character from each selected set
    password = [random.choice(char_set) for char_set in char_sets]
    all_chars = ''.join(char_sets)
    password += [random.choice(all_chars) for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)

def main():
    length, use_upper, use_lower, use_digits, use_special = get_user_choices()
    if length < (use_upper + use_lower + use_digits + use_special):
        print("Error: Password length too short for the selected options.")
        return
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()