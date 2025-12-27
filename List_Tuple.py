friends = ["Prachi", False, 17.00, 26]

print(friends[0])

# lists are mutable and every operation changes the original list

friends[1] = True

print(friends[0:2])

friends.append("Kaisy")
print(friends)

l1 = [2, 17, 12, 26, 1, 27]

l1.sort()
print(l1)

l1.insert(2, 45)  # index: 2 inserted: 45
print(l1)

l1.reverse()
print(l1)

print(l1.pop(-2))
print(l1)

l1.remove(45)
print(l1)


List1 = [1, 2, 3, 4]
List2 = [1, 2, 3, 4]

# List1.append(List2)
# print(List1)

List1.extend(List2)
print(List1)