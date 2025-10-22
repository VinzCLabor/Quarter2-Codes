def calculate_delivery_fee(distance, rate):
    return distance * rate

distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

Tdf = calculate_delivery_fee(distance, rate)
print("Total Delivery Fee: ₱", Tdf)
