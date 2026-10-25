
# A program that calculates the price after discount

price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))

reduction = price * discount / 100
price_with_discount = price - reduction

print(f'Price with discount: {price_with_discount}')
print(f'Reduction: {reduction}')
