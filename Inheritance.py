class employee: # Base class

    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


    def __init__(self):
        print("Contructor of employee")

    @classmethod
    def show(cls):
        print({cls.a}) # will only show class attributes over instance attributes\

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = employee()
e.a = 45

e.name = "Prachi Shende"
print(e.fname, e.lname)

class coder:
    def __init__(self):
        print("Contructor of coder")

    language = "Python"
    def printLanguage(self):
        print(f"Out of all languages, here is your language: {self.language}")

# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
#

# class programmer(employee): # Derived class/ Child class, single inheritance
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"the name if the programmer is {self.name} and she is good in {self.language} language")


class programmer(employee, coder): # multiple inheritance
    def __init__(self):
        print("Contructor of programmer")

    company = "ITC Infotech"


# multilevel inheritance

class manager(programmer):
    def __init__(self):
        # print("Contructor of Manager") # for normal execution of constructor
        super().__init__()
        print("Contructor of Manager") # for the execution of parent class's constructor also
    c = 3



a = employee()
print(a.company)
a = manager()

b = programmer()

print(a.company, b.company)

# operator overloading

class number:
    def __init__(self):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = number(1)
m = number(2)