from collections import OrderedDict


def count_char(str1):
    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    chars = {}
    for char in str1:
        if char in chars:
            chars[char] += 1
        else:
            chars.update({char: 1})
    print(chars)
    chars_sort = OrderedDict(sorted(chars.items()))
    print(chars_sort)


count_char("Hello world")
