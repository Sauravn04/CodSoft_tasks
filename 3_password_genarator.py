import string
import secrets


def generate_password(len, use_num=True, use_symbol=True):
    char = string.ascii_letters
    if use_num:
        char += string.digits
    if use_symbol:
        char += string.punctuation

    password = "".join(secrets.choice(char) for i in range(len))
    return password


def main():
    try:
        len = int(input("Enter desire password length: "))
        use_num = input("Include numbers (y/n)? ").lower() == "y"
        use_symbol = input("Include symbols (y/n)? ").lower() == "y"

        strong_pass = generate_password(len, use_num, use_symbol)
        print("Genrated password:", strong_pass)
    except ValueError:
        print("Invalid input.Please enter a valid positive integer in password length.")


if __name__ == "__main__":
    main()
