total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid Number")
    number = int(input("Number of items: "))
for i in range(number):
    price = int(input("Price of item:"))
    total += price
print()
print(f"Total price for {number} items is $ {total}")


