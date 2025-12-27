a = (1, 2, 3, 1)
print(a)
print(type(a))

# collection but mutable structure is tuple

b = (1,) # empty tuple with 1 element

print(a.count(1))
print(a.index(1))

repeated = a * 3
print(repeated)

c = a + b
print(c)

print(2 in b)
print(2 in a)

print(max(a))
print(a[1:3])
