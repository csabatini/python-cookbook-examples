# underneath, Counter stores # of occurrences as values mapped to keys (words) in a dict
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
print word_counts.most_common(1)
print '-' * 20

for word, count in word_counts.items():
    print '%s - %d time(s)' % (word, count)
# you're - 1 time(s)
# eyes - 8 time(s)
# look - 4 time(s)
# don't - 1 time(s)
# into - 3 time(s)
# under - 1 time(s)
# not - 1 time(s)
# the - 5 time(s)
# my - 3 time(s)
# around - 2 time(s)
