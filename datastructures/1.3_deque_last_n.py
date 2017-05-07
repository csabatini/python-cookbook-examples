from collections import deque


# Keeping a limited history is a perfect use for a collections.deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    word = 'justice'
    with open('files/usdeclar.txt') as f:
        for line, prevlines in search(f, word, 5):
            for pline in prevlines:
                print pline
            print line + '\n' + ('-' * 20)
