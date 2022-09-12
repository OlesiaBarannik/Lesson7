

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

total_prices = {}

for key in stock:
    values = stock[key] * prices[key]
    total_prices[key] = values

print(total_prices)
