class Employee:
    company = "ITC"
    name = "default name"
    salary = "1200000"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary {self.salary}")

class Coder:
    language = "Python"
    def printlang(self):
        print(f"Out of the all languages here is your languages {self.language}")
class Programmer(Employee , Coder): #here the programmer contains all the properties and the methods of the employee and coder calss
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name of the company {self.company}  is and the salary {self.salary} ")

a =  Employee()
b = Programmer()
b.printlang()
b.show()
b.showlanguage()

