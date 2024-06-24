def extract_name_from_email(email):

    name = email.split('@')[0]


    name_parts = name.split('.')
    capitalized_name = ' '.join(part.capitalize() for part in name_parts)

    return capitalized_name


def main():
    email_dict = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        name_from_email = extract_name_from_email(email)


        confirm = input(f"Is your name {name_from_email}? (Y/n) ").strip().lower()

        if confirm == "" or confirm == "y":
            name = name_from_email
        else:
            name = input("Name: ").strip().title()

        email_dict[email] = name

    print("\nList of users:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
