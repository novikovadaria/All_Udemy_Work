number = 1001
print(id(number))
print(id(1001))

a = 2
print("a:", id(a))

a = a + 1
print("a1:", id(a))
print("three", id(3))

b = 2
print("b:"(id(b)))
print("two:", id(2))

smt = 12
smt = "Zhenya"
smt = ["a", 2, True]


def zhenya():
    print("Good girl")


smt = zhenya
smt()


def outer():
    outer_n = 100
    print(id(outer_n))

    def inner():
        inner_n = 200
        inner_n = "Zhenya"
        print("Inner number", inner_n)
    inner()


outer()

global_n = 300
