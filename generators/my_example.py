def get_divisible_numbers(number):
    while True:
        if number % 9 == 0 and number % 11 == 0:
            yield number
        number += 1


if __name__ == '__main__':
    # start at a low number
    low_generator = get_divisible_numbers(1)

    print next(low_generator)
    print next(low_generator)
    print next(low_generator)
    # 99
    # 198
    # 297

    # start at a high number
    high_generator = get_divisible_numbers(2000)

    print next(high_generator)
    # 2079
