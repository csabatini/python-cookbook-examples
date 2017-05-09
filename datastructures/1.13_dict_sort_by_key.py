rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# sorted() uses timsort algorithm
rows_by_lname = sorted(rows, key=lambda x: x['lname'])

print rows_by_lname
# [{'lname': 'Beazley', 'uid': 1002, 'fname': 'David'},
#  {'lname': 'Cleese', 'uid': 1001, 'fname': 'John'},
#  {'lname': 'Jones', 'uid': 1003, 'fname': 'Brian'},
#  {'lname': 'Jones', 'uid': 1004, 'fname': 'Big'}]
