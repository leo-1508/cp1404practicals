from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A special version of a Taxi with additional fanciness and flagfall charges."""

    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)  # Call the Taxi's constructor
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # Scale the price per km by fanciness

    def get_fare(self):
        """Return the price for the taxi trip, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
