import random
from taxi import Car  # Assuming the Car class is defined in taxi.py

class UnreliableCar(Car):
    """An Unreliable Car that only drives based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)  # Call the Car's constructor
        self.reliability = reliability  # Set the reliability attribute

    def drive(self, distance):
        """Drive the car a given distance if it's reliable enough."""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            # The car drives the requested distance
            return super().drive(distance)
        else:
            # The car doesn't drive at all due to unreliability
            return 0  # Distance driven is 0
