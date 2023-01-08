#Lambda function, map(), reduce(), filter(), void -- Anonymous function
x = lambda a: a + 10
a = int(input())
print(x(a))

#________________________________

#oops - object oriented programming

''' 
Abstraction - work which happens in background which we dont need to know. Hiding of irrelevent data.
Encapsulation - bringing all the data under one roof. eg: dictionary. Wrapping of all the data into one group.
Polymorphism - deals with multiple forms. something which is able to perform multiple tasks. (will deal with functions)
Inheritance - multiple child tasks. aquiring multiple values from someone. (will deal with classes). code re-usability is good.
1 : Class - blueprint of the object.
2 : Object - has certain attributes/behaviour.
'''
#class definition
class Car:
    h = 10
    w = 20
maruti = Car() #object creation
print(maruti.h) #passing value
print(maruti.w) #passing value

#________________________________________

class Student:
    def __init__(self,name,reg):
        self.name = name
        self.reg = reg

    def pr(self):
        print('Hello my name is', self.name)

obj = Student('Anurag',4115007)
print(obj.name)
print(obj.reg)
obj.reg=233                     # over-writing
print(obj.reg)
obj.pr()

#__________________________________________

'''
init helps the class initialize
object's attributes
and is called everytime an object is created from a class

2 : by using self keyword you can easily access all the object defined within the class including functions.
'''
#__________________________________________

def square(n):
    for i in range (1,n+1):
        if i == 1 or i == n:
            print('*'*n)
        else:
            print('*'+' '*(n-2)+'*')
n = int(input())
square(n)
