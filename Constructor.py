class Employee:
    language = 'python' #this is class attributes
    salary = '120000'

    def __init__(self, name , salary , language): #This is called dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("This is init constructor in python")

harry = Employee('piyush' , '5000000' , 'Machine learning')
print(harry.name,harry.salary,harry.language)
#instance get more prefrence then class , thats why the language is print