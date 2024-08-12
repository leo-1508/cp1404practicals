from silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi with a fanciness of 2
fancy_taxi = SilverServiceTaxi("Luxury Car", 100, 2)

# Drive the taxi 18 km
fancy_taxi.drive(18)

# Print the details of the SilverServiceTaxi
print(fancy_taxi)

# Calculate the fare and print it
fare = fancy_taxi.get_fare()
print(f"Fare: ${fare:.2f}")

# Assert the fare is as expected (should be $48.78 for 18 km with fanciness 2)
assert fare == 48.78, f"Expected fare: $48.78, but got: ${fare:.2f}"

# Additional assertions to verify the functionality
assert fancy_taxi.price_per_km == 2.46, f"Expected price_per_km: $2.46, but got: ${fancy_taxi.price_per_km:.2f}"
assert fancy_taxi.flagfall == 4.50, f"Expected flagfall: $4.50, but got: ${fancy_taxi.flagfall:.2f}"
