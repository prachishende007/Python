s = {1, 5, 7}

# elements don't repeat, unordered, unindexed

e = set() # empty set

print(s, type(s))
s.add(3)
print(s)
print(len(s))

s.remove(5)
print(s)

s.pop() # removes random element
s.clear()

s1 = {1, 3, 4, 9}
s2 = {2, 5, 3, 7, 8}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1.issubset(s2))
print({1,3}.issubset(s1))
