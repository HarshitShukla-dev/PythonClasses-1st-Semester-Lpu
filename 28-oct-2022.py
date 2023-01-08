import math
x = min(1,2,3)
y = max(1,2,3)
print(x)
print(y)
a = math.sqrt(81)
print(a)
b = math.floor(1.4)
print(b)

#_______________________________________

#for loop
#intialization
#termination
#increament/decrement

#_________________________________________

student = ["anurag","vishal","ankit","binod"]
for i in student:
    print(i)

#__________________________________________

for i in "anurag":
    print(i)

#___________________________________________

#tuple-datatype-unchangable-concatination is possible
a=('anurag','harshit','vishal')
print(a)
print(type(a))

#___________________________________________

#set-datatype-unordered-unchangable

a={'anurag','harshit','vishal'}
a.add('virus')
print(a)

#____________________________________________

#dictionary-ordered-changable-no duplicate-keys and values

a={
    'name':"anurag",
    'company':'cipherschools',
    'college':"IIT"
}
print(a['name'])
print(a.keys())

#______________________________________________

x=bin(int(input("x: "))).replace("0b","")
y=oct(int(input("y: "))).replace("0o","")
print(x,y,sep=",")