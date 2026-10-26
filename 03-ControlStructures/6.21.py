amount = int(input("Enter the amount in PLN: "))
original = amount

coin5 = amount // 5
amount = amount % 5

coin2 = amount // 2
amount = amount % 2

coin1 = amount

print(f"The amount of PLN {original} in coins:")
print(f"5 PLN coins: {coin5}")
print(f"2 PLN coins: {coin2}")
print(f"1 PLN coins: {coin1}")