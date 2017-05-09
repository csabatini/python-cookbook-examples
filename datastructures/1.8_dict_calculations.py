prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

inverted = zip(prices.values(), prices.keys())

print inverted
# [(37.2, 'HPQ'), (10.75, 'FB'), (612.78, 'AAPL'), (205.55, 'IBM'), (45.23, 'ACME')]

print min(inverted)
# (10.75, 'FB')

print max(inverted)
# (612.78, 'AAPL')
