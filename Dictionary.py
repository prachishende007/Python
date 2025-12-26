marks = {
    "Prachi": 97,
    "P": 79,
    "S":67
}

# key: value pairs, unordered, mutable, indexed

print(marks, type(marks))
print(marks["Prachi"])
print(marks.items())
print(marks.keys())
print(marks.values())
print(len(marks))

marks.update({"Prachi": 99, "T": 54})
print(marks)

print(marks.get("Prachi"))  # prints none if key not exists
print(marks["Prachi"])      # prints error if key not exists

# marks.clear()

new_dict = marks.copy()

my_list = ["Prachi", 17.00]

new_dict1 = dict.fromkeys(my_list, 0)
print(new_dict1)

print(marks.pop("Prachi"))