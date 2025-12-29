class employee:
    language = "Py"
    salary = 1500000

    def getInfo(self):
        print(f"the technology is {self.language}.")

    # static method
    @staticmethod
    def greet():
        print("Good Morning!")

    # Constructor : DUNDER method double underscore
    def __init__(self, name, salary, language): # automatically called only init is called automatically
        print("This is an object")
        self.name = name
        self.salary = salary
        self.language = language

# salary is class attribute and name is object/instance attribute
prachi = employee()
prachi.name = "Prachi"
prachi.language = "LLM"
print(prachi.name, prachi.language)

prachi.getInfo()
# this gets converted into employee.getInfo(prachi)

rohit = employee()
rohit.name = "Rohit"
print(rohit.name, rohit.language)


