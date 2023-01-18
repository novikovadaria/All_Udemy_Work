# if 2 > 1 # Syntax Error
from timeit import timeit
import sys

list = [1, 2]
print(list[3])  # Expeptions (logical errors)

age = int(input('age: '))  # if you provide a sring it will be an error

# ...........................Try....Except.............
try:
    age = int(input('Age: '))
except:
    print('please enter a valid age')
print('No exceptions here')

# ..........................Try....Excep......Else......
try:
    age = int(input('Age: '))
except ValueError:
    print('please enter a valid age')
else:
    print('No errors here')

# .................
try:
    age = int(input('Age: '))
except ValueError as exp_error:
    print('please enter a valid age')
    print(exp_error)
else:
    print('No errors here')

# ....................................
random_list = ['a', 0, 2]
for entry in random_list:
    try:
        print('The entry is:', entry)
        r = 1 / int(entry)
        break
    except:
        print('OOPS!', sys.exc_info()[0], 'occured.')
        print('next entry.')
print()
print('The reciprocal of', entry, 'is', r)

# Get a ZeroDivisionErrer
try:
    age = int(input('Age: '))
    x = 10 / age
except ValueError:
    print('Please enter a valid age')
else:
    print('No errors here')

# resolving
try:
    age = int(input('Age: '))
    x = 10 / age
except ValueError:
    print('Please enter a valid age')
except ZeroDivisionError:
    print('Age cannot be zero')
    print('Please enter a valid age')

else:
    print('No errors here')

# Creating a tuple of errors
try:
    age = int(input('Age: '))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print('Please enter a valid age')
except ZeroDivisionError:
    print('Age cannot be zero')
else:
    print('No errors here')

# ................
try:
    note = open('someFile.txt')
    age = int(input('Age: '))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print('Enter a valid age')
else:
    print('No errors here')
    note.close()
finally:
    note.close()

# ........................
try:
    with open('someFile.txt') as note:
        print('note opened')
    age = int(input('Age: '))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print('Please enter a valid age')
except FileNotFoundError:
    print('oops')
else:
    print('No errors here')

# Multiple Files
try:
    with open('someFile.txt') as note, open('anotherFile.txt') as my_note:
        print('note opened')
    age = int(input('Age: '))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print('Please enter a valid age')
except FileNotFoundError:
    print('oops')
else:
    print('No errors here')

# Raising exceptions


def calculate_age(age):
    if age <= 0:
        raise ValueError('age cannot be zero or less')
    return 10 / age


calculate_age(0)

# Handling


def calculate_age(age):
    if age <= 0:
        raise ValueError('age cannot be zero or less')
    return 10 / age


try:
    calculate_age(0)
except ValueError as error:
    print(error)

# Bad sides of exceptions
