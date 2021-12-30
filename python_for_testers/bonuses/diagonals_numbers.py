import math


def sum_diagonals_of_spiral(size):
    n = 1
    step = 2
    total = 0
    since_last = 0
    while n <= size ** 2:
        total += n
        n += step
        since_last += 1
        if since_last == 4:
            step += 2
            since_last = 0
    return total


print(sum_diagonals_of_spiral(5))


# way2 - Lior
def sum_diagonals_of_spiral2(size):
    num = 1
    numbers = [1]
    for i in range(1, math.ceil(size / 2)):
        for j in range(1, 5):
            num += i * 2
            numbers.append(num)

    return sum(numbers)


print(sum_diagonals_of_spiral2(1001))
