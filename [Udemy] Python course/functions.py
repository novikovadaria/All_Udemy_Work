# ...........defining..........
from tomlkit import date


def book():
    print("Thriller")


book()
# .........
success = True


def operation():
    if success:
        print("Yay!!!")


operation()
# ............


def sum():
    for number in range(4, 34, 4):
        print(number)


sum()

# ................Function parameters and arguments............


def arithmetic_operations(x, y):
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} + {y} = {x + y}")


arithmetic_operations(20, 5)
arithmetic_operations(112, 32)

# ...............


def legal_age(name, age, allowed_age):
    if age >= allowed_age:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")


legal_age("Dasha",  17, 18)
legal_age("Sarah", 22, 18)

# ...........................Functions types...............


def facebook(name, status):
    return f"{name} is {status}"


user_status = facebook("Zhenya", "offline")
print(user_status)

# keyword arguments


def multiply(number, by):
    return number * by


result = multiply(15, 4)
print(result)

# ..................required and optional parameters.........
# optional ones
# optinal parameneter should be the last one


def working_condition(device, status="working"):
    # "working" is default now
    return f"The {device} is {status}"


print(working_condition("drill press"))
print(working_condition("welding maching", "out of order"))

# ......................non-keyword parameneter.................
# fun(*...)


def sum(x, y):
    return x + y

# print(sum(89, 98))
# print(sum(89,98,23,56,45))


def num(*number):
    return number


print(num(10, 21, 65, 112, 555, 666))

# .....................


def subtract(*nums):
    number = 100
    for x in nums:
        number -= x
    return number


print(subtract(2, 3, 5, 25, -45))

# .........................Keyword agruments..............


def employee(**info):
    print(info)


employee(name="Dasha", l_name="Novikova", age=17, skill_set="cat")
# ................


def to_do(**to_do_status):
    return to_do_status


to_do_status_result = to_do(
    get_coffe="Done", exercise="Pending", watch_tv="In progress")
print(to_do_status_result)

# .............................Scope................


def message(date):
    content = "something very coll has happend"


message("May 22, 2100")
# print(date) NameError

# ................................
# def comment (date):
#     content = "Amazing landscape"

# comment("May 1, 2011")
# print(date)
# print(content)

# Global var
content = "just do it"


def post(date):
    content = "i am on a trip"


post("01.01.1970")
# print(content)

# global..................................
dog_name = "Hachi"


def animal_names():
    global dog_name
    dog_name = "Georgie"


animal_names()
print(dog_name)

# .............................................Debbuging.....................


def subtract(*nums):
    target_num = 1000
    for x in nums:
        target_num -= x
        return target_num


print(subtract(50, 24, 123, 321))
