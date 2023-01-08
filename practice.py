n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ", end=' ')
    for l in range(1,i+1):
        print(l, end=' ')
    for m in range(i-1,0,-1):
        print(m,end=' ')
    print()

#_____________________________________________\

import time
currentTime=time.time()
ts=int(currentTime)
cs=ts%60
tm=ts//60
cm=tm%60
th=tm//60
ch=th%24
print(ch,cm,cs)

#________________________________

#guess a no
import random
a=random.randint(0,99)
b=-1
while b!=a:
    b=int(input("enter ur guess: "))
    if b==a:
        print("nyc job")
    elif b>a:
        print("your guss is too high")
    else:
        print("print ur guess is too low")

#_______________________________________

#factor

a=int(input("enter:"))
x=1
for i in range(1,a+1):
    if a%i==0:
        x=x*i
print(x)

#_______________________________________

x=input("x:")
y=input("y:")
z=x+y
print(f'x={x},y={y},z={z}')

#________________________________________

p=float(input("p:"))
q=int(input("q:"))
print(f'p={p:.6f},q={q},product={p*q}')

#_______________________________________________

