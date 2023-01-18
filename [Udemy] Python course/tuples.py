# unchangeble
first_tuple = ()
print(first_tuple)

num = (1, 2, 3)
print(type(num))

# can have different types of data inside

mixed = ({"name": "Saitama"}, [1, 2, 3], (23, 4.3), True, "Asia")
print(mixed)

# packing
to_do = "buy coffe", 'read a book', 'finish homework'
print(to_do)
# still tuple

# unpacking
to_do1, to_do2, to_do3 = to_do
print(to_do1)
print(to_do2)
print(to_do3)

# one element
name = ("Tommy")
print(name)
print(type(name))

name = ("Tommy",)
print(name)
print(type(name))

# Acessing tuple items
# indexing
mixed_tuple = (False, 3.14159, "Python", ["Web", "Mobile"])
print(mixed[0])
print(mixed[4])

# Negative indexing
print(mixed[-1])
print(mixed[-5])

# Slicing
print(mixed[0:2])
print(mixed[2:4])
print(mixed[:4])

# Changing Tuples
numbers = (4, 2, 3, [5, 6, 7, 8])
# numbers[1] = 10
print(numbers)
numbers[3][2] = 111
print(numbers)

# Reassignment
numbers = (222, 333, 444)

# Repeatimg a tuple items
print(('Movie', ) * 5)

# Concatenation
letters = ('p', 'y', 't', 'h', 'o', 'n')
mixed = numbers + letters
print(mixed)

# Deleting
del letters
print(letters)

# Methods
# count()
names = ("Dasha", "Daria", 'Alina', 'Zhenya', 'Dasha')
print(names.count('Dasha'))

# index()
print(names.index('Dasha'))

# Operations
# Membership

print('Dasha' in names)

# Iterating
for name in names:
    print(name)
    print("I like the name", name)
