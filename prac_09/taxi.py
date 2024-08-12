class Car:
    """Represent a car object."""

    def __init__(self, name, fuel):
        """Initialize a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23  # Class variable shared by all instances

    def __init__(self, name, fuel):
        """Initialize a Taxi instance."""
        super().__init__(name, fuel)  # Call the parent class's constructor
        self.current_fare_distance = 0  # Initialize the current fare distance

    def drive(self, distance):
        """Drive the car a given distance."""
        distance_driven = super().drive(distance)  # Call the drive method from Car
        self.current_fare_distance += distance_driven  # Add the distance to the fare distance
        return distance_driven

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Start a new fare."""
        self.current_fare_distance = 0  # Reset the fare distance

    def __str__(self):
        """Return a string representation of the Taxi."""
        return f"{super().__str__()}, fare distance={self.current_fare_distance}, fare=${self.get_fare():.2f}"
