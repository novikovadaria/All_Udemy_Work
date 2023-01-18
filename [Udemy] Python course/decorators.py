# a functions with different names
def name1(name):
    print(name)


name1('John')

name2 = name1
name2('Jane')

# higher oreder functions


def increment(x):
    return x + 1


def decrement(x):
    return x - 1


def operation(result, x):
    output = result(x)
    return output


number_inc = operation(increment, 50)
number_dec = operation(decrement, 10)
print(number_dec)
print(number_inc)

# a function returning another function


def operation():
    def increment():
        print('The numver has been added')
    return increment


number_inc = operation()
number_inc()

operation()()

# ........................................Decorator...............
# __call__() ->> callable


def operation(func):
    def increment():
        print('before the func')

        func()

        print('after the func')
    return increment


def decrement():
    print('The number has been decremented')

# operation(decrement)


# the syntactic sugar of a decorator
decorated_function = operation(decrement)
decorated_function()


def operation(func):
    def increment():
        print('before the func')

        func()

        print('after the func')
    return increment


@operation
def decrement():
    print('The number has been decremented')


decrement()

# ...............Decorating functions with parameters........
# def operation(x,y):
#     return x / y
# print(operation(101,32))

# using a decorator


def operation(func):
    def inner(x, y):
        print(f'{x} / {y} = ')
        if y == 0:
            print('cannot devided be zero')
            return

        return func(x, y)
    return inner


@operation
def divide(x, y):
    print(x/y)


divide(2, 5)

# ..............................Arguments...........


def multiply(func):
    def digits(*args):

        func(*args)
    return digits


@multiply
def operation(x, y, z):
    print(x * y * z)


operation(10, 20, 30)

# Keywords args


def do_arithmetic(func):
    def number(**kwargs):
        func(**kwargs)
    return number


@do_arithmetic
def operation(x, y, z, a, b, c, m, n, o):
    print(((a/b) * m + z*n + (x/o+y) / c+m*n+o) / o - n)


operation(x=100, y=100, z=300, a=400, b=500, c=600, m=700, n=800, o=900)

# ............................Chainig Decorators......


def info_last_name(func):
    def full_name(*args):
        func(*args)
    return full_name


@info_last_name
@info_last_name
def info(name, lastname):
    print(f'my full name is {name}, {lastname}')


info('Muslim', 'Halyle')
