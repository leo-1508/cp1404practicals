import random

def get_score(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):

    print("*" * int(score))

def get_valid_score():

    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Score must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score

def main_menu():

    print("\nMain Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input(">>> ").upper()
    return choice

def main():

    user_score = None

    user_score = get_valid_score()

    while True:
        choice = main_menu()

        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            if user_score is not None:
                result = get_score(user_score)
                print(f"Result: {result}")
            else:
                print("Please get a valid score first.")
        elif choice == "S":
            if user_score is not None:
                print("Stars:")
                print_stars(user_score)
            else:
                print("Please get a valid score first.")
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
