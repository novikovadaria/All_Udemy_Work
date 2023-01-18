first_set = {21, 32, 54, 665, 999}
print(first_set)

# unordered
# can have differenet types of data
numbers = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
print(numbers)

# Set Method
colors = set(('blue', 'red', 'green', 'blue'))
print(colors)

colors = set(['blue', 'red', 'green', 'blue'])
print(colors)


colors = set({
    'blue': 1,
    'red': 2,
    'green': 3
})
print(colors)

# cannot have a mutable data type as an item
# Empty set
names = {}
print(type(names))

numbers = set()
print(type(numbers))

# Modifying Sets
mixed_info = {'Python', 'Dog'}
# mixed_info[1]

# add()
mixed_info.add(31)
print(mixed_info)

# update()
mixed_info.update([12, 'jar', 'sand'])
print(mixed_info)

mixed_info.update(['bird', 'island'], ('cat', 'island'), {'rabbit', 'island'})
print(mixed_info)

# removimg items
# discard()
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)
numbers.discard(4)
print(numbers)

# item that doesnt exist
numbers.discard(11)
print(numbers)

# remove()
numbers.remove(5)
print(numbers)
# item that doesnt exist
# numbers.remove(11)
# print(numbers)

# pop()
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)

# clear()
numbers.clear()
print(numbers)

# Set Operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union()
print(A | B)
print(A.union(B))

# intersection
print(A & B)
print(A.intersection(B))

# defference()
print(A - B)
print(B-A)
print(A.difference(B))
print(B.difference(A))

# symmetric difference
print(A ^ B)
print(B ^ A)
print(B.symmetric_difference(A))

# copy()
numbers = {101, 202, 303, 404, 505, 606}
other_numbers = numbers
print(other_numbers)

numbers.remove(606)
print(other_numbers)

other_numbers.discard(505)
print(numbers)

some_numbers = numbers.copy()
print(some_numbers)
print(numbers)

some_numbers.add(909)
print(numbers)
print(id(other_numbers))

# disjoined()
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}
D = {10, 20, 30, 7}

A.isdisjoint(B)  # True
A.isdisjoint(C)  # False

# issubset()
print(A.issubset(B))
print(A.issubset(C))
print(B.issubset(A))

# issuperset()
print(A.issuperset(B))
print(B.issuperset(A))

# Membership
numbers = {1, 2, 3, 4}
print(1 in numbers)
print(6 in numbers)

# Iterating
for num in numbers:
    print(num)

# Frozen Sets
numbers = frozenset([1, 2, 3, 4, 5, 6])
print(numbers)

some_nums = frozenset([3, 4, 5, 6])
print(numbers.isdisjoint(some_nums))
print(numbers.difference(some_nums))

# frozenset()
vowels = ('a', 'e', 'i', 'o', 'u')
frozen_vowels = frozenset(vowels)
print(frozen_vowels)

# Set Comprehensions
number1 = {number ** 2 for number in range(10)}
print(number1)
numbers2 = {numbers2 ** 3 for number in range(5)}
print(numbers2)
