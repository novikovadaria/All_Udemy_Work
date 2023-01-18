# __iter__() & __next__
numbers = [1, 2, 3, 4, 5]
first_iterator = iter(numbers)
print(next(first_iterator))

# next() == __next__()
print(first_iterator.__next__())
print(type(first_iterator()))

# using a for loop()
for number in numbers:
    print(number)

# ............................The work of a foor loop
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

iterable_obj = iter(numbers)

# infinite while loop
while True:
    try:
        element = next(iterable_obj)
        print(element)
    except StopIteration:
        break

# ...........................Buiding a custom iterator................


class NumberPower:
    def __init__(self, maxi_num):
        self.maxi_num = maxi_num

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.maxi_num:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration


num_pow = NumberPower(2)

iterable_data = iter(num_pow)
print(next(iterable_data))

for i in NumberPower(4):
    print(i)

# ...............................Infinite iterators.........................
# print(int())
number = iter(int, 1)
print(next(number))

for element in number:
    print(element)


class OddNums:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


odd_nums = OddNums()
iterable_nums = iter(odd_nums)
print(next(iterable_nums))
