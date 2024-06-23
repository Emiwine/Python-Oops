class Employee:  #here we make the class with name of Employee
    language = 'python' #This is class attribute
    salary  = 1200000

harry = Employee()
harry.name = 'harry' #This is the object attribute
print(harry.language,harry.salary,harry.name)

rohan = Employee()
rohan.name = 'auysh'
print(rohan.name,rohan.language,rohan.language,rohan.name)

#here names are the object or instance attribute and the language and salary are the class attributes as they directly belongs to the class