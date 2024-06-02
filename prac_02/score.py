import random

def evaluate_score(score):
    """
    Evaluate the given score and return the result.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """
    Main function to interact with the user and generate a random score.
    """
    user_score = float(input("Enter score: "))
    while user_score >= 0:
        result = evaluate_score(user_score)
        print(result)
        user_score = float(input("Enter score: "))
    
    # Generate a random score
    random_score = random.randint(0, 100)
    random_result = evaluate_score(random_score)
    print(f"Random Score: {random_score}, Result: {random_result}")

if __name__ == "__main__":
    main()
