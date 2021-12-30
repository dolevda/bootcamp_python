countries = ["Greece", "India", "USA", "England", "Austria"]
print(countries[:3])

print("Befor change", countries)
temp = countries[0]
countries[0] = countries[1]
countries[1] = temp
print("After change", countries)

countries.reverse()
print("Revers:", countries)

countries.sort()
print("Sort:", countries)

last_index = len(countries)-1
last_country = countries[last_index]

#pop
countries.pop(last_index)

#Remove
#countries.remove(last_country)
print("After removed:", countries)


middle_index = len(countries)/2
countries.insert(int(middle_index), "Italy")
print("After insert:",countries)



