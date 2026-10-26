current_price = 140.00
previous_price = 200.00

price_drop = previous_price - current_price
percentage = (price_drop / previous_price) * 100

print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

if percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(percentage)}%")