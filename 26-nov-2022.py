#sort list
l = []
n = int(input("Enter length of list: "))
for i in range(1,n+1):
    a = int(input("Enter "+str(i)+" digit : "))
    l.append(a)

for i in range(0,n-1):
    for j in range(0,n-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]

print(l)

#______________________________________________________

a = 45673
b = (a//10000)**(a%10)
print(b)
if b%2 == 0:
    print('even')
else:
    print('odd')

#______________________________________________________

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print('\r')
pattern(5)

#______________________________________________________

