class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary {self.salary}")

class Programmer(Employee):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name of the employee is {self.name} and the salary {self.salary}")

a =  Employee()
b = Programmer()

print(a.company,b.company)