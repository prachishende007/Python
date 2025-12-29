# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# s = "Prachi"
# f = open("file.txt", "w")
# f.write(s)
# f.close()

f = open("file.txt")
# line = f.readline()

# lines = f.readlines()
# print(line, type(line))

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

s = " Hey! there!"
f = open("prachi.txt", "a")

f.write(s)

f.close()


# with statement
with open("prachi.txt") as f:
    print(f.read())

# don't need to close the file here

