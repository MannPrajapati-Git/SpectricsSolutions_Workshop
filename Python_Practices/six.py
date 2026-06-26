# 6. Create a list of 5 floats representing prices. Print the highest price using if-else (not max()).

prices = []
for i in range(5):
    price = float(input("Enter price : "))
    prices.append(price)

highest = 0
for price in prices:
    if price > highest:
        highest = price

print("Prices : ", prices)
print("Highest price : ", highest)
