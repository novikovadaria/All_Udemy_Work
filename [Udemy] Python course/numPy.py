from http.client import _DataType
import numpy as np

# creating array
array = np.array([1, 2, 3])
print(array)
print(type(array))


# multidimensional array
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(array)
print(array.shape)

# Helper Methods
# zeros()
array = np.zeros((4, 6))
print(array)

# ones()
array = np.ones((4, 6))
print(array)

# full()
array = np.full((4, 6), 11)
print(array)

# random.random()
array = np.random.random((4, 6))
print(array)

# accesing
print(array[0, 0])

# comparison operator
print(array > 0.5)

# boolean indexing
print(array[array > 0.3])

# Array computational functions
# sum()
array = np.random.random([2, 3, 4, 6, 7.8, 5.5, 3.4])
print(np.sum(array))

# floor()
print(np.floor(array))

# ceil() # the opposite of floor
# round()

# Arithmetic operations
# print(array1 + array2)
