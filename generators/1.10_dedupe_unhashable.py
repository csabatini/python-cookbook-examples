# dictionaries are mutable/unhashable and can't be used in a set
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

generator_one = dedupe(a, key=lambda d: d['x'])

print next(generator_one)
print next(generator_one)
print '-' * 20

generator_two = dedupe(a, key=lambda d: d['x'])

for pair in generator_two:
    print pair
# {'y': 2, 'x': 1}
# {'y': 4, 'x': 2}
