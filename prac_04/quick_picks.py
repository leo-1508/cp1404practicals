import random

# Constants for the number range and the number of picks per line
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(format_quick_pick(quick_pick))

def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

def format_quick_pick(quick_pick):
    return " ".join(f"{number:2}" for number in quick_pick)

main()

