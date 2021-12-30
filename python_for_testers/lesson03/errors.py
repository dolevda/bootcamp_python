def print_massage(text):
    try:
        massage = text + " OK"
        print(text)
    except TypeError as e:
        print("Type error then we do casting to str! ", e)
        massage = str(text) + " OK"
        print(massage)


print_massage(234)


#Q2
try:
    my_list = [1, 2, 0]
    my_list[6] = my_list[1] / my_list[2]
    print(my_list)
except IndexError:
    print("You list's index is out of bound")
except ZeroDivisionError:
    print("You can't divide number by zero")

#output will be ""You can't divide number by zero"