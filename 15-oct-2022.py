import random
a=random.randint(1,8)
print(a)

#_____________________________

a="""hi my name is smriti shukla,
i am at lpu campus
and we are learning python"""
print(a)

#______________________________

#slicing
b="cipher schools"
print(b[2:5])

#______________________________

c="cipHerSchooL"
print(c.lower())
print(c.upper())
print(c.replace("ci",""))
a=""
for i in range(-1,-len(c)-1,-1):
    a=a+c[i]
print(a)

#______________________________

x="cipher"
y="school"
print(x+y)

#_______________________________

i=1
while i < 10:
    print(i)
    i+=1

#________________________________

i=1
while i < 8:
    print(i)
    if i == 3:
        break
    i+=1

#__________________________________

import random
print("Welcome to the game")
while True:
    uC = input("Enter Rock/Paper/Scissor/close : ")
    cC=["rock","paper","scissor"]
    cS=random.choice(cC)
    print(f"\n user choice is {uC} and computer choice us {cS} \n")
    if uC == cS:
        print("Tie")
    elif uC=="rock" and cS=="paper":
        print("computer won")
    elif uC=="scissor" and cS=="paper":
        print("user won")
    elif uC=="paper" and cS=="rock":
        print("user won")
    elif uC=="rock" and cS=="scissor":
        print("user won")
    elif uC=="scissor" and cS=="rock":
        print("computer won")
    elif uC=="paper" and cS=="scissor":
        print("computer won")
    elif uC=="close":
        print("game over")
        break
    else:
        print("Wrong choice enter again!!! ")
