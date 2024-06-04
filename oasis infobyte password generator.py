import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+{}[]'

def generate_password(length, include_letters, include_numbers, include_symbols):
    char_set = ''
    if include_letters:
        char_set += letters
    if include_numbers:
        char_set += numbers
    if include_symbols:
        char_set += symbols

    if not char_set:
        print("Error: No character types selected. Please select at least one character type.")
        return ""
    
    password = ''.join(random.choice(char_set) for _ in range(length) )
    return password

def main():
    print("Welcome to the PyPassword Generator!")

    length = int(input("Enter the total length of the password: "))
    include_letters = input("Do you want to include letters? (Y/N): ").strip().lower() == 'y'
    include_numbers = input("Do you want to include numbers? (Y/N): ").strip().lower() == 'y'
    include_symbols = input("Do you want to include symbols? (Y/N): ").strip().lower() == 'y'

    if length <= 0:
        print("Error: Password length must be greater than 0.")
        return

    password = generate_password(length, include_letters, include_numbers, include_symbols)
    
    if password:
        print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
