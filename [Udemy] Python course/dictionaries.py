

from hashlib import new


contacts = {
    "Dasha": 456,
    "Zhenya": 123
}

print(contacts)

# ........
employee_info = {"Nmae": "Will",
                 "Last Name": "Willson",
                 "Adress": "NYC",
                 "Age": 31
                 }

# dict()
animal_names = dict(cat="Sebastian", dog="Togo")
print(animal_names)

# ..............
print(employee_info["Name"])
print(employee_info["Age"])
employee_info["Adress"] = "Katkovo"
employee_info['Hobbies'] = "Reading, Walking"
print(employee_info)

print(employee_info["Colour"])
# 1 - cheking whether a key exists
if "Colour" in employee_info:
    print('Colour')

# 2 - get()
print(employee_info.get("Colour"))

# .........
print(employee_info.get("Colour", "Green"))

# Methods
# clear()
employee_info.clear()
print(employee_info)

# copy()
gerald_info = employee_info.copy()
gerald_info["Colour"] = "Red"
print(gerald_info)
print(employee_info)

# fromkeys()
letters = {'a', 'i', 'e', 'o', 'u'}
numbers = [1, 2]
vowels = dict.fromkeys(letters, numbers)
print(vowels)

print({}.fromkeys(employee_info))

# items and keys methods
print(employee_info.items())

del employee_info['Colour']
print(employee_info.items())

# keys()
print(employee_info.keys())

del employee_info["Name"]
print(employee_info.keys())

# values()
print(employee_info.values())
del employee_info["Age"]
print(employee_info.values())

# popitem()
print(employee_info.popitem())
# returns and pops

# setdefault()
print(employee_info.setdefault('Age'))
# 34

# pop()
# -1
target_item1 = employee_info.pop('Age')
print(target_item1)
print(employee_info)

# -2
target_item2 = employee_info.pop('Smoking', 'No')
print(target_item2)
print(employee_info)

# -3
target_item3 = employee_info.pop('Adress', 'Sochi')
print(target_item3)
print(employee_info)

# update()
# -1
lost_key = {'Favourite Movie': "Blood diamond"}
employee_info.update(lost_key)
print(employee_info)

# -2
found_key = {'Favourite Movie': "Titanic"}
employee_info.update(found_key)
print(employee_info)

# -3
employee_info.update(dog_name='Krypto', bird_name="Precious")
print(employee_info)

# Comprehension
coordinates = {}
for x in range(5):
    coordinates[x] = ((x*5)/2 + 12) - (2.4/1.2)*6
print(coordinates)

coordinates = {x: ((x*5)/2 + 12) - (2.4/1.2)*6 for x in range(5)}
print(coordinates)

old_p = {"milk": 1.02, "coffe": 2.5, "bread": 1.89}
dollars_to_pound = 0.76
new_price = {item: value * dollars_to_pound for (item, value) in old_p.items()}
print(new_price)

# ........
original_dict = {"Jack": 38, "Lincoln": 48, "Theodore": 57, "John": 33}
even_dict = {k: v for (k, v) in original_dict.items() if v/2 == 0}
print(even_dict)

# multiple comprehension
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

new_d = {k: 'old' if v > 40 else "young" for (k, v) in original_dict.items()}
print(new_dict)

# nested
# new_dict ={
#     k1 :{k2:k1*k2 for k2 in range(1,6) for k1 in range(2,5)}
# }
# print(new_dict)

new_dict = {}
for k1 in range(2, 5):
    new_dict[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print(new_dict)

# complete unfolded
new_dict = {}
for k1 in range(2, 5):
    new_dict[k1] = {}
    for k2 in range(1, 6):
        new_dict[k1][k2] = k1*k2
print(new_dict)

random = {
    1: 456,
    2: 123,
    45: "Hey"
}
for key in random:
    print(key)

for i in random:
    print(random[i])
