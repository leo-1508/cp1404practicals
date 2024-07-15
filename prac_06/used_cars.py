"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" that is initialized with 100 units of fuel.
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to this new car object.
    limo.add_fuel(20)

    # Print the amount of fuel in the car.
    print(f"Limo has fuel: {limo.fuel}")

    # Attempt to drive the car 115 km.
    limo.drive(115)

    # Print the limo object to check the __str__ method.
    print(limo)


if __name__ == '__main__':
    main()
