a = [1, 5, 2, 1, 9, 1, 5, 10]

# if items are hashable, easiest deduping option is usually to create a set
print set(a)
print '-' * 20


# if order is important, it can be done with a set and a generator
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


gen_function = dedupe(a)

print next(gen_function)
print next(gen_function)
print next(gen_function)
print next(gen_function)
print next(gen_function)
# StopIteration
print '-' * 20

for num in dedupe(a):
    print num
# 1
# 5
# 2
# 9
# 10
