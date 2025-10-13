distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

total_fee = distance * rate

print("Total Delivery Fee: ₱", round(total_fee, 2))
