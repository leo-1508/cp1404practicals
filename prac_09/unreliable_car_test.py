from unreliable_car import UnreliableCar

# Create an UnreliableCar with 50% reliability
my_unreliable_car = UnreliableCar("Old Car", 100, 50)

# Attempt to drive 40 km
distance_driven = my_unreliable_car.drive(40)
print(f"Drove {distance_driven} km. Car details: {my_unreliable_car}")

# Attempt to drive another 100 km
distance_driven = my_unreliable_car.drive(100)
print(f"Drove {distance_driven} km. Car details: {my_unreliable_car}")
