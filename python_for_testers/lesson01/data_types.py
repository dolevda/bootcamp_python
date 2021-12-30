# Q1
first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
age = int(input("Enter your age: "))

print(str(age))
print(first_name.upper())
print(last_name.lower())
print(first_name[1:])
print(last_name[:-1])

# Q2
text = "Python is a general purpose computer programming language"
print("The sum of times that computer is shoe is: ", text.count("computer"))
print("The index that computer is shoe is: ", text.index("computer"))
print(text.replace(" ", ""))

# Q3
text2 = "Hello World"
index_of_space = text2.find(" ")
print(text2[index_of_space+1:])