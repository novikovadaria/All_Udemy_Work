# ...................... Filter Function
from sys import getsizeof
from array import array
from tkinter import N


letters = ['a', 'b', 'c', 'd', 'e', 'i', 'j', 'o']


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter in vowels:
        return True
    else:
        return False


filtered_vowels = filter(filter_vowels, letters)
print(filtered_vowels)
for vowel in filtered_vowels:
    print(vowel)

# .........
random_list = [1, 0, 'a', False, True, '0']
filtered_list = filter(None, random_list)
print("Thruthy values are")
for value in filtered_list:
    print(value)

# ................................Anonymous Function
products = [
    ('Product -1', 15),
    ('Product -2', 25),
    ('Product -3', 5),
    ('Product -4', 45),
    ('Product -5', 20),
    ('Product -6', 30)
]

products.sort(key=lambda product: product[1])
print(products)

# lambda + filter()
my_list = [1, 5, 4, 6, 8, 11, 3, 12, 34, 55]
new_list = filter(lambda x: (x % 2 == 0), my_list)
for num in new_list:
    print(num)

# even_nums = list(new_list)
# print(even_nums)


new_list = list(map(lambda x: x*2, my_list))
print(new_list)

# .............................Map Function
# Iterable
numbers = (1, 2, 3, 4, 5)

# Function


def calculate_square(n):
    return n*n


result = map(calculate_square, numbers)
print(result)

# Converting a map object to a set
num_square = set(result)
print(num_square)
# Converting a map object to a set, tuple, list (the same way)

# lambda + map
numbers = (1, 2, 3, 4, 5)
letters = ['a', 'b', 'c']
# result = map(lambda x: x, letters)
# result = map(lambda x: x * x, numbers)

# Passing multiple iterables
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [7, 8]
result = map(lambda n1, n2: n1 + n2, numbers1, numbers2)
print(tuple(result))

# ...........................Zip  Function
numbers_list = [1, 2, 3]
names_list = ['Adriana', 'Cecile', 'Darcey']
result = zip()
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(numbers_list, names_list)
result_set = set(result)
print(result_set)

# Different number of iterables
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names_list = ['Adriana', 'Cecile', 'Darcey']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX')

result = zip(numbers_list, numbers_tuple)
result_set = set(result)
print(result_set)

result = zip(numbers_list, names_list, numbers_tuple)
result_list = list(result)
print(result_list)

# Unzipping the values using the zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
print(result_list)

unzipped_coordinates, unzipped_values = zip(*result_list)
# unzipped iterables are converted to a tuple
print("unzipped coordinates:", unzipped_coordinates)
print("unzipped coordinates:", unzipped_values)

# ..........................Arrays..............
numbers = array('i', [1, 2, 3])
numbers.append(4)
print(numbers)

numbers[0] = 2.3  # TypeError

# ..........................Generator Expressions............
# list comprehension
numbers = [x * 2 for x in range(15)]
print(type(numbers))
for x in numbers:
    print(x)

# generator object
numbers = (x*2 for x in range(15))
print(numbers)
print(type(numbers))

for y in numbers:
    print(y)

numbers = (x*2 for x in range(10))
print('Generatir object:', getsizeof(numbers))
numbers_list = [x*2 for x in range(10)]
print('LCE:', getsizeof(numbers_list))

# Unpacking operator *
numbers = [1, 2, 3]
print(numbers)

print(*numbers)
values = range(15)
print(values)

values = list(range(15))
print(values)
print(*values)

print({*'python'})

cities = ['Rome', 'Athens', 'Istanbul', 'Tokyo', 'Jakarta']
names = ['Olivia', 'Amelia', 'Oliver', 'Charlotte', 'Liam']
info = [*names, *cities]
print(info)

dict_one = {
    'name': 'Jasper',
    'city': 'Tokyo',
}
dict_two = {
    'full name': 'Dick Van Dyke',
    'address': 'USA',
}
dict_three = {
    'name': "William",
    'job': 'Developer'
}

combined = {**dict_one, **dict_two, 'country': 'France', **dict_three}
print(combined)

# ................................Recursive Functions..................


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))


num = 2
print('the factorial of', num, 'is', factorial(num))
