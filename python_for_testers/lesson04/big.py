
def fins_big_num(list1):
    if len(list1) == 0:
        return ("The list is empty")
    big_num = list1[0]
    for num in list1:
        if num > big_num:
            big_num = num
    return big_num

