# ......................Classes.............
# object
# 1-attributes
# 2-behaviour
# A classes is a blueprint for creating objects

from collections import namedtuple


class Robot:
    pass


# Object/Instance
# An object (instance) is an instantation of a class
robot_obj = Robot()
print(robot_obj)
print(type(robot_obj))

# class of int for creating integers(whatever)
x = 25
print(type(x))

# Creating classes


class Robot:
    def walk(self):
        print('The robot is walking')


robot = Robot()
robot.walk()
print(type(robot))

# isinstance()
print(isinstance(robot, Robot))
robot_obj = Robot()
print(isinstance(robot_obj, Robot))

# ....................................Constuctors..................
# class Robot:
#     def walk(self):
#         print('The robot is walking')

# robot = Robot()
# robot.walk()
# robot = Robot(2.3, 6.5)


class Robot:
    def __init__(self, x, y):
        pass

    def walk(self):
        print('The robot is walking')


robot = Robot(2.3, 6.5)

# ............


class Robot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f'Walking coordinates ({self.x}, {self.y})')


robot = Robot(1.3, 11.2)
robot.walk()


# ...............Instance Attributes VS Attributes..............
# 1 - Instance Attr
# 2 - Class Attr

# Instance Attr
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(print(f'Walking coordinates ({self.x}, {self.y})'))


# 1st Instantiation
test_walk1 = Robot(8.7, 99.7)
test_walk1.walk()
print(test_walk1.x)
print(test_walk1.y)

# Different Instance attr
test_walk1.z = 2.3
print(test_walk1.z)

# 2nd Instantiation
# Class Attr


class Robot:
    # class attr
    coordinates_z = 45.87

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(print(f'Walking coordinates ({self.x}, {self.y})'))


# ............intance methods VS class methods............
# intance methods

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f'Walking coordinates ({self.x}, {self.y})')


test_walk = Robot(1.1, 4.6)
test_walk.walk()

# Class Method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f'Walking coordinates ({self.x}, {self.y})')
    # decorate

    @classmethod
    def specific_coordinate(cls):
        return cls(1.1, 4.6)


test_walk = Robot.specific_coordinate
test_walk.walk()

# ....................................Magic Method.................


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'I am a magic method with  coordinates ({self.x}, {self.y}'

    def walk(self):
        print(f'Walking coordinates ({self.x}, {self.y})')


test = Robot(0.1, 0.5)
print(test)

print(str(test))

# Comparing objects


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


test = Robot(4.015, 9.2345)
other_test = Robot(4.015, 9.2345)

print(test == other_test)
print(id(test))
print(id(other_test))

# __eq__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


test = Robot(4.015, 9.2345)
other_test = Robot(4.015, 9.2345)
print(test == other_test)

# __gt__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


test = Robot(15, 35)
other_test = Robot(4.015, 9.2345)
print(test > other_test)

# __lt__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


test = Robot(15, 35)
other_test = Robot(4.015, 9.2345)
print(test < other_test)

# ............................Arithmetic Operating Methods............

# __add__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'coordinates ({self.x + other.x},{self.y+other.y})'


test = Robot(12, 1)
other_test = Robot(4.12, 8.45)
print(test + other_test)

# __sub__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return f'coordinates ({self.x - other.x},{self.y - other.y})'


test = Robot(12, 1)
other_test = Robot(4.12, 8.45)
print(test - other_test)

# __mul__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return f'coordinates ({self.x * other.x},{self.y * other.y})'


test = Robot(12, 1)
other_test = Robot(4.12, 8.45)
print(test * other_test)

# __floordiv__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return f'coordinates ({self.x  // other.x},{self.y // other.y})'


test = Robot(12, 1)
other_test = Robot(4.12, 8.45)
print(test // other_test)

# .................................Custom Container....................
# creating
# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}
#     def add(self, bookmark):
#         self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0)+1
# target_bookmark = BookmarkedPage()
# target_bookmark.add('Python')
# target_bookmark.add('Python')
# target_bookmark.add('Python')

# print(target_bookmark.bookmarks)


class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(
            bookmark.lower(), 0)+1


target_bookmark = BookmarkedPage()
target_bookmark.add('Python')
target_bookmark.add('Python')
target_bookmark.add('Python')

print(target_bookmark.bookmarks)

# Getting the count of key


class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0)+1

    def __getitem__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)


target_bookmark = BookmarkedPage()
target_bookmark.add('Python')
target_bookmark.add('Python')
target_bookmark.add('Python')

print(target_bookmark.bookmarks)
print(target_bookmark.bookmarks['Python'])

# Getting number


class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0)+1

    def __getitem__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.bookmarks)


target_bookmark = BookmarkedPage()
target_bookmark.add('Python')
target_bookmark.add('Python')
target_bookmark.add('Python')

print(target_bookmark.bookmarks)
print(target_bookmark.bookmarks['Python'])
print(len(target_bookmark))
# Iterating


class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0)+1

    def __getitem__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.bookmarks[bookmark.lower()] = count

    def __iter__(self):
        return iter(self.bookmarks)


target_bookmark = BookmarkedPage()
target_bookmark.add('Python')
target_bookmark.add('Python')
target_bookmark.add('Python')

print(target_bookmark.bookmarks)
for bookmark in target_bookmark:
    print(bookmark)

# Blocking


class BookmarkedPage:
    def __init__(self):
        self.__bookmarks = {}

    def add(self, bookmark):
        self.__bookmarks[bookmark] = self.__bookmarks.get(bookmark, 0)+1

    def __getitem__(self, bookmark):
        return self.__bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.__bookmarks[bookmark.lower()] = count

    def __iter__(self):
        return iter(self.__bookmarks)


target_bookmark = BookmarkedPage()
target_bookmark.add('Python')
target_bookmark.add('Python')
target_bookmark.add('Python')
# target_bookmark.bookmarks
# target_bookmark.__bookmarks
# print(target_bookmark.bookmarks)

# Accesing
print(target_bookmark.__dict__)

# .......................Class Property and Property Decorator...........


class MovieRating:
    def __init__(self, rating):
        self.rating = rating


movie_rating = MovieRating(10)

# .............


class MovieRating:
    def __init__(self, rating):
        self.rating = rating

    def get_rating(self):
        return self.__rating

    def set_rating(self, value):
        if value < 0:
            raise ValueError('Movie rating cannot be less than zero')
        self.__rating = value


movie_rating = MovieRating(8)

# Decorating


class MovieRating:
    def __init__(self, rating):
        self.rating = rating

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError('Movie rating cannot be less than zero')
        self.__rating = value

# Inheritance


class John:
    def sing(self):
        print('Singing')

    def run(self):
        print('Running')


class Jane:
    def sing(self):
        print('Singing')

    def jog(self):
        print('Jogging')

# define a parent/base class


class Person:
    def sing(self):
        print('Singing')
# sub/child/devired classes


class John:
    def run(Person):
        print('Running')


class Jane:
    def jog(Person):
        print('Jogging')


runner = John()
runner.sing()

jogger = Jane()
jogger.sing()

# Attr


class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print('singing')


class John:
    def run(Person):
        print('Running')


class Jane:
    def jog(Person):
        print('Jogging')


runner = John()
runner.employed


# Object Class
print(isinstance(Person, object))
print(issubclass(John, Person))

# Overriding


class Person:
    def __init__(self):
        self.employed = True
        print('Base class')

    def sing(self):
        print('singing')


class John(Person):
    # overriding methods
    def __init__(self):
        super().__init__()
        print('Sub Class')
        self.jogger = True

    def run(self):
        print('Running')


runner = John()
print(runner.jogger)

# Multiple Inheritance


class Person():
    def sport_status(self):
        print('Runner')

    def sport_status(self):
        print('Jogger')


# class Jane (Person, John):
#     pass
# jane = Jane()
# jane.sport_status()

# Data Classes
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


robot1 = Robot(1, 2)
robot2 = Robot(1, 2)
print(id(robot1, robot2))

# __eq__


def __eq__(self, other):
    return self.x == other.x and self.y == other.y


robot1 = Robot(1, 2)
robot2 = Robot(1, 2)
print(robot1 + robot2)

# nametuple()
Robot = namedtuple('Robot', ['x', 'y'])
robot1 = Robot(x=1, y=2)
robot2 = Robot(x=1, y=2)
print(robot1 == robot2)
