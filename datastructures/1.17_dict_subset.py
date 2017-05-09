prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

high_prices = {k: v for k, v in prices.items() if v > 200}
print high_prices
# {'AAPL': 612.78, 'IBM': 205.55}

tech_symbols = ['AAPL', 'IBM', 'HPQ', 'MSFT']
tech_prices = {k: v for k, v in prices.items() if k in tech_symbols}
print tech_prices
# {'HPQ': 37.2, 'AAPL': 612.78, 'IBM': 205.55}
