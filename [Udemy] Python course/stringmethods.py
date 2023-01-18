# 1 - len()
address = "Sochi"
print(len(address))

# 2 - [] Notation
print(address[0])
print(address[4])

# 3 - [] Notation
print(address[0:4])

# 4 - Concatenation
country = "Japan"
city = "Tokyo"
full_address = city + ", " + country
print(full_address)

# 5 - upper
print(address.upper())

# 6 - lower()
print(city.lower())

# 7 - title()
print(full_address.title())

# 8 - strip()
anime = "                  Steins Gate         "
print(anime.strip())
print(anime.lstrip())
print(anime.rstrip())

# 9 - find()
print(address.find("o"))

# 10 - replace()
print(address.replace("S", "F"))

# 11 - in operator
print("ne" in address)
print("o" in address)

# 12 - not operator
print("ne" not in address)
print("o" not in address)
