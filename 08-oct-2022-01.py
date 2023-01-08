a=10
b=20
c=pow(a+b,2)
print(c)

#________________________________

#conditonal statements, 
#based on certain conditions , we perform actions on those certain conditions

a=10
b=20
if b>a:
    print("b is actually greater than a")

#_________________________________

if 5>6:
    print(" is bigger")
else:
    print("6 is bigger")

#__________________________________

a=10
b=20
if b>a:
    print("b>a")
elif a==b:                                      #also known a conditional statement ladder
    print("a=b")
else:
    print("a>b")

#__________________________________

smriti=50
if smriti>90:
    print("Congrats u have A+")
elif smriti>80 and smriti<=90:
    print("congrats A")
elif smriti>70 and smriti <=80:
    print("congrats b")
else:
    print("C")

#_________________________________

#even perfect square
l = int(input("enter1"))
r = int(input("enter2"))
for i in range(l, r + 1):
    if (i**(.5) == int(i**(.5))) and i%2==0:
        break
    else:
        print(i)
 
#____________________________________________