file = 'test1.txt'


def write_something(file_name):
    my_file = open(file_name, "w")
    my_file.write("Try to write1\n")
    my_file.write("Try to write2")
    my_file.close()


write_something(file)


def read_something(file_name):
    my_file = open(file_name, "r")
    data_file = my_file.read()
    print(data_file)


read_something(file)


# way2
def file_read(file_name):
    with open(file_name, "r") as my_file:
        data = my_file.read()
        print(data)
