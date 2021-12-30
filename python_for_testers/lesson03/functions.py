# Q1
def revers_str(str1):
    revers = ""
    len_str = len(str1)
    while len_str > 0:
        revers += str1[len_str - 1]
        len_str = len_str - 1
    print(revers)


revers_str('dolev345')


# Q2
def biggest_two(num1, num2):
    if num1 > num2:
        return num1
    return num2


def biggest_three(num1, num2, num3):
    return biggest_two(num1, (biggest_two(num2, num3)))


print(biggest_three(3, 9, 8))


# Q3
def unique_numbers(list1):
    new_list = []
    for elem in list1:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


list1 = [1, 2, 2, 3, 3, 3, 3, 5, 6, 7]
print(unique_numbers(list1))


# Q4

def print_factorial(num):
    factorial = 1
    if num < 0:
        print("Negative number")
    elif num == 0:
        print("Factorial of 0 is :1")
    else:
        while num > 0:
            factorial = factorial * num
            num = num - 1

    print("The factorial is:", factorial)


print_factorial(5)
