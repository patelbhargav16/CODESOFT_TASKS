import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 45)
    print("       PYTHON PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length <= 0:
                print("Password length must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        again = input(
            "\nDo you want to generate another password? (y/n): "
        ).lower()

        if again != "y":
            print("\nThank you for using the password generator!")
            break


if __name__ == "__main__":
    main()