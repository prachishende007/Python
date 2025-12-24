name = "Prachi"
age = input("Enter age : ")

# strings are immutable everytime, every operation it creates a new string

print(name)
print(age)

# Slicing:
print(name[1:5])
print(name[1:5:2])

# Operations:
print(len(name))
print(name.replace("Pra", "Ru"))
print(name.endswith("chi"))
print(name.startswith("pra"))
print(name.capitalize())
print(name.lower())
print(name.upper())

print(name.isalpha())

print(f"Hey {name}, your age is {age}")


