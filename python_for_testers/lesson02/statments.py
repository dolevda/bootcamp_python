# Q1
x = 1.2
y = 3.2

if y < x:
    print(x)
elif y > x:
    print(y)
else:
    print(x + y)

# Q2

numbers = [2, 5, 9]
if numbers[0] > numbers[1]:
    print("First is bigger:", numbers[0])
elif numbers[0] < numbers[1]:
    print("Second is bigger:", numbers[1])
else:
    print("Numbers is equals!")

numbers[0] = 5
print(numbers)

numbers[0] = 8
print(numbers)

print("----------------------")
# Q3
index = 1
for index in range(11):
    print(index + 1)

index = 1
while index <= 10:
    print(index)
    index = index + 1
    for index in range(30, 50):
        if index % 2 == 0:
            print(index)

for index in range(20, 40):
    if index % 2 == 1:
        print(index)

# Q4
countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
for country in countries:
    print(country)

for country in countries:
    if country == "Israel":
        print(country)

if countries[2] == 'Peru':
    print("yes its there")
else:
    print("No,sorry ...")

print(len(countries[0]))

# Q5
age = int(input("Please enter number between 0 to 120: "))
if 0 < age <= 6:
    print("Go to Kindergarten")
elif 6 < age <= 18:
    print("Go to School")
elif 18 < age <= 67:
    print("Go to Work")
elif 67 < age <= 120:
    print("Collect your pension")

# way1
get_num = int(input("Please enter number between 0 to 120: "))
match get_num:
    case get_num if 0 < get_num <= 6:
        print("Go to Kindergarten")
    case get_num if 7 <= get_num <= 18:
        print("Go to School")
    case get_num if 19 <= get_num <= 67:
        print("Go to Work")
    case get_num if 68 <= get_num <= 120:
        print("Collect your pension")

# way2
get_num = int(input("Please enter number between 0 to 120: "))
match get_num:
    case get_num if get_num in range(0, 6):
        print("Go to Kindergarten")
    case get_num if get_num in range(7, 18):
        print("Go to School")
    case get_num if get_num in range(19, 67):
        print("Go to Work")
    case get_num if get_num in range(68, 120):
        print("Collect your pension")

# Q6
profession = input("What is your profession (teache/bank telle/qa/average salary)? ")
if profession.lower() == "qa":
    print(15000)
elif profession.lower() == "teache":
    print(5000)
elif profession.lower() == "bank telle":
    print(10000)
elif profession.lower() == "average salary":
    print(10000)
else:
    print("Unknow")

# Q7

names = {123: "dolev", 2: "sali", 3: "dani"}
for name in names.keys():
    print(name)
for name in names.values():
    print(name)

# Q8
numbers = {3, 2, 15, 30, 77, 12}
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(num)

# Q9
word = ['o', 'l', 'l', 'e', 'h']
while len(word) > 0:
    print(word.pop(), end=" ")
print()

# 10
numbers = [15, 2, 36, 20, 7]
if numbers[0] > numbers[1]:
    if numbers[0] > numbers[2]:
        print(numbers[0])
    else:
        print(numbers[2])
else:
    if numbers[1] > numbers[2]:
        print(numbers[1])
    else:
        print(numbers[2])

big_num = numbers[0]
for num in numbers:
    if num > big_num:
        big_num = num
print("The biggest num is :", big_num)

total = 0
for num in numbers:
    total += num
print("The total sum od numbers is :", total)

number = int(input("Please enter number to check if is prime: "))
is_prime = True
for x in range(2, int(number/2)):
    if number % x == 0:
        is_prime = False
        break

if is_prime:
    print("The number is prime")
else:
    print("The number is prime")
