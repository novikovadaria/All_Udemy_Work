#  a nested function
def person(adress):
    def john():
        print(adress)
    john()


person('USA')

# nonlocal variable


def outer():
    number = 85

    def inner():
        nonlocal number
        number = 95
        print('inner function:', number)
    inner()
    print('outer function:', number)


outer()

# defining a clouser


def person(address):
    def john():
        print(address)
    return john


john_address = person('usa')
john_address()

# deleting the original/enclosing scope
del person()
john_address()

# .........................using closure..............


def numbers(n):
    def multiply_by(x):
        return x * n
    return multiply_by


three = numbers(3)
four = numbers(4)
print(three)
print(three(10))

# print(numbers.__closure__)
# print(three.__closure__)
