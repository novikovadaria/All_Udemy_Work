# ......................Loops..............
for x in range(10):
    print(x)

for number in range(5):
    print(f"The code has run for {number} time(s)")

for a in range(5, 15):
    print(a)

# .....................................step.............
for a in range(0, 100, 10):
    print(a)

# break method
status = True
for number in range(1, 4):
    print(f"Attempt {number}")

    if status:
        print("Success")
        break
else:
    print("Failed")

# ...............................Nested loops...............
# for x in range(3):
#     for y in range(6):
#         print(x,y)

for x in range(5):
    for y in range(2):
        for z in range(3):
            print(x, y, z)

# ...............................Iterables...........
print(type(range(5)))

for char in "Dasha Novikova":
    print(char)

for something in ["Coffee", "Play with a cat"]:
    print(something)

# ..................................While loops...........
temp = 40
while temp >= 20:
    print(f"its a good day to go out when the temp is {temp}")
    temp -= 5

# ..........................Infinite loops..........
number = 100
while number > 1:
    print(number)
    number -= 10
