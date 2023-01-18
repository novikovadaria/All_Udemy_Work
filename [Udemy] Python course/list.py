# List of identical items
animal = ["cats"] * 10
print(animal)

# Merging/concatenation
even_nums = [2, 3, 4, 5, 10]
odd_nums = [8, 9, 4, 5, 7]
cities = ["Tokio", 'London', 'Katkovo']
mixed_data = even_nums + odd_nums + cities
print(mixed_data)

# List Method
numbers = list(range(100))
print(numbers)

random_name = list("zhenya")
print(random_name)
print(len(random_name))

# .............
collection = [23, 'm', 8, 'ofofo']
collection[5] = "Python"
print(collection[0])

# Range
print(collection[0:2])

# step
# print(collection[::2]) прыжок в два
# print(collection[::3]) прыжок в три
# print(collection[::-1]) задом наперёд
# print(collection[2::2]) прыжок в два начиная с третьего элемента

# Unpacking
numbers = [23, 49, 85]
num1, num2, num3 = numbers
print(num2)
print(num1)
print(num3)

# .......
numbers = [23, 45, 67, 84, 2]
num1, num2, *other_nums = numbers
print(num1)
print(num2)
print(other_nums)

# ...........
num1, *other_nums, num2 = numbers
print(num1)
print(num2)
print(other_nums)

# ..........
num1, num2, *other_nums, num3, num4 = numbers
print(num1)
print(num2)
print(other_nums)
print(num3)
print(num4)

# looping
letters = ["a", 'b', 'c']
for letter in letters:
    print(letter)

# Enumerating
for letter in enumerate(letters):
    print(letter)

# ..............
items = (0, "a")
index, letter = items
print(index, letter)

for index, item in enumerate(letters):
    print(index, item)

# Modifying List Items
number = [1, 2, 3]
names = ['Zhenya', 'Dasha']
fruits = ['Apple', 'Banana']
names.append('Senya')
print(names)

# insert()
fruits.insert(1, 'Lemon')
print(fruits)

# pop()
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)

# remove()
fruits.remove("Banana")
print(fruits)

# del statement
del numbers[0:4]
print(numbers)

# clean()
print(fruits.clear())

# reverse()
names.revers()
print(names)

# join()
print(" ".join(names))

# Find index
# index()
print(fruits.index("Lemon"))

# Existing
if "Mango" in fruits:
    print(fruits.index("Mango"))

# count()
print(fruits.count("Lemon"))

# Sorting List
# sort()
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

# sorted()
print(sorted(numbers))

# def sort_ptoducts(product):
#   return product[1]

# products.sort(key=sort_products)
# print(...)

# Comprehension
numbers2 = [num for num in numbers]
print(numbers2)

numbers2 = [num*2 for num in numbers]
print(numbers)

fruits2 = [fruit.lower() for fruit in fruits]
print(fruits2)

# Single Condition

# items = [item[1] for item in products if items[1] >= 20]
# print(items)

# Double Condition
modified_numbers = [num if num > 100 else num/2 for num in numbers]
print(modified_numbers)

# Swapping List Items
smt = [2, 4, 6]
number[0], number[1], number[2] = number[2], number[1], number[0]
