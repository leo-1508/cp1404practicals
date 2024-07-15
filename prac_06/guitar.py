
class Guitar:
    def __init__(self, name="", year=0, cost=0):

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):

        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):

        current_year = 2024
        return current_year - self.year

    def is_vintage(self):

        return self.get_age() >= 50


def main():
    # Create instances of Guitar
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2015, 3000.00)

    # Print the details of each guitar
    print(guitar1)
    print(guitar2)

    # Print the age and vintage status of each guitar
    print(f"The age of {guitar1.name} is {guitar1.get_age()} years")
    print(f"Is the {guitar1.name} vintage? {guitar1.is_vintage()}")

    print(f"The age of {guitar2.name} is {guitar2.get_age()} years")
    print(f"Is the {guitar2.name} vintage? {guitar2.is_vintage()}")


if __name__ == "__main__":
    main()
