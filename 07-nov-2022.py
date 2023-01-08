#defining the fn
def harshit():
    print('Hi I am a user defined function Harshit')
#calling the fn
harshit()

#_____________________________________

#parameterised fn and non parameterised fn

#_____________________________________

def harshit2(name):
    print("hello my name is "+ name)
harshit2('harshit')

#_____________________________________

def pr(fname,lname):
    print('my name is',fname,lname)
pr("harshit","shukla")

#_____________________________________

def pr(*name): #adding star made it tuple
    print("my name is "+name)
pr("anurag",'misrha','cypher','schools')

#_____________________________________

def pr(name1,name2,name3): 
    print("my name is "+name1)
pr(name1='anurag',name2='cipher',name3='schools')

#_____________________________________

def pr(name):
    for i in name:
        print(i)
name=['anurag','harshit','cipher','schools']
pr(name)

#_____________________________________

def pr(n):
    return n*5
print(pr(5))

#_____________________________________

#recursion - function calls itself to perform the task
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
print(factorial(4))

#_____________________________________

def sum(x):
    if x<=1:
        return 1
    else:
        return x+sum(x-1)
print(sum(5))

#_____________________________________

