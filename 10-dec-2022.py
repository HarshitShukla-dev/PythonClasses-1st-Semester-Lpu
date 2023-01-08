#Inheritance - multiple child tasks. aquiring multiple values from someone.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)

class Employees(Person):
    pass

a = Employees("Smriti","20")
a.display()

#_______________________________________________________________

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)

class Employee(Person):
    def __init__(self,name,age):
        Person.__init__(self,name,age)

a = Employee("Anurag","20")
a.display()

#_______________________________________________________________

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

class Employee(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year = year

        def welcome(self):
            print("Hi welcome ",self.name,"whose age is",self.age,"to the year",self.year)

a = Employee("Anurag",28,2004)
a.welcome()