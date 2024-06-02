num = int(input("Number of items: "))
total = 0
for i in range(num):
    price = float(input("Price of item: $"))
    total += price
if total > 100:
    total *= 0.9
print(f"Total price for {num} items are:" + format(total, ".2f"))
