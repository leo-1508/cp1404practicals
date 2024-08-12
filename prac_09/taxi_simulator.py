from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()

        if user_choice == "q":
            break
        elif user_choice == "c":
            current_taxi = choose_taxi(taxis)
        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def choose_taxi(taxis):
    """Display available taxis and let the user choose one."""
    print("Taxis available: ")
    display_taxis(taxis)  # Corrected function name here
    taxi_choice = input("Choose taxi: ")
    try:
        taxi_choice = int(taxi_choice)
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input; please enter a number.")
        return None

def drive_taxi(taxi, total_bill):
    """Drive the chosen taxi and return the updated bill."""
    distance = input("Drive how far? ")
    try:
        distance = float(distance)
        taxi.start_fare()  # Start a new fare before driving
        taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        return total_bill + trip_cost
    except ValueError:
        print("Invalid input; please enter a number.")
        return total_bill

def display_taxis(taxis):
    """Display the list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()
