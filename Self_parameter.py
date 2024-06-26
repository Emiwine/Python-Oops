class Employee:
    language = 'python'
    salary = '1200000'

    def getinfo(self):
        print(f'The language is {self.language}. The salary is {self.salary}')
    @staticmethod #This is also called decorator
    def greet(): #some times we need the function that donot contain self parameter then we can define as @static method
        print('Good morning')


harry = Employee()
harry.language = 'java'  #this is object and it got high preference
harry.getinfo()
harry.greet()