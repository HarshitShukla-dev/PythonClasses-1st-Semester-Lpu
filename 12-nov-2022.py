#simple calculator
def sum(a,b):
    print(a+b)
def sub(a,b):
    print(abs(a-b))
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
while True:
    a = int(input("Enter first digit: "))
    b = int(input("Enter second digit: "))
    c = input("Enter choice (+,-,/,*) : ")
    if c == "+":
        sum(a,b)
    elif c == '-':
        sub(a,b)
    elif c == '*':
        multiply(a,b)
    elif c == '/':
        divide(a,b)
    else:
        pass
    while True:
        x = input("coninue? (y/n) : ")
        if x == 'n' or x == 'N':
            m = 0
            break
        elif x == 'y' or x == 'Y':
            m = 1
            break
        else:
            print("Wrong choice ..... Enter again !!! ")
            continue
    if m == 0:
        break
            
#_________________________________________________________

#program to check even odd

a = int(input())
if a%2==0:
    print("even")
else:
    print("odd")

#_________________________________________________________

#prime number
a = int(input("Enter number: "))
s = 0
if a > 1:
    for i in range(2,a):
        if a%i == 0:
            s = 1
            break
if s == 1 or a <= 1:
    print('not prime')
else:
    print('prime')

#_________________________________________________________

#Armstrong
a = b = int(input("Enter no : "))
d = 0
c = str(len(a))
while a > 0:
    x = a%10
    d += x**c
    a = a//10
if d == b:
    print("Armstrong")
else:
    print("Not Armstrong")

#_________________________________________________________

#pallindrom
a = input("Enter String: ")
b = ""
for i in range(-1,(-(len(a)+1)),-1):
    b += a[i]
if a == b:
    print("Pallindrom")
else:
    print("Not pallindrom")

#_________________________________________________________

