def get_password(min_length):
    password = input("Enter your password: ")
    while len(password) < min_length:
        print(f"Your password must be at least {min_length} characters long.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    print("*" * len(password))

def main():
    min_length = 6
    password = get_password(min_length)
    print_asterisks(password)

if __name__ == "__main__":
    main()
