mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print [x for x in mylist if x > 0]
# [1, 4, 10, 2, 3]

print [x for x in mylist if x < 0]
# [-5, -7, -1]

# one downside to list comprehension is a large result depending on the input
# alternatively, a generator expression can be used
positives = (n for n in mylist if n > 0)

for x in positives:
    print x
