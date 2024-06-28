class Employee:
    language = 'python' #this is class attributes
    salary = '120000'

harry = Employee()
harry.language = 'machine learning' #this is objects attributes
print(harry.language,harry.salary)
#instance get more prefrence then class , thats why the language is print