name = input("Enter your name: ")

def display_menu():
    print("\nWelcome!", name)
    print("1.Press (H)ello")
    print("2.Press (G)oodbye")
    print("3.Press (Q)uit")

def main():
    display_menu()
    choice = input("Enter your choice: ")
    while choice != "Q":
        if choice == "H":
            print(f"Hello, {name}")
        elif choice == "G":
            print(f"Goodbye, {name}")
        else:
            print(f"Invalid message, try again")
        display_menu()
        choice = input("Enter your choice: ")
    print("Finished!")
if __name__ == '__main__':
    main()