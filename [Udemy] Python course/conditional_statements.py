"""
if (boolean expression):
    execute the statements
"""
# ..............................Chek for a single condition
temp = 24

if temp > 30:
    print("Cats are happy")

print("I dont care")

# ..................................Chek for 2 condition
if temp > 25:
    print("Awesome")
else:
    print("Cold")
# .......................else (в противном случае)
# ..............................Chek for multiple conditions
temp = 25
if temp >= 35:
    print("Hot")
elif temp > 25:
    print('Awesome')
elif temp < 20:
    print("Cold")
else:
    print("Undecided")
