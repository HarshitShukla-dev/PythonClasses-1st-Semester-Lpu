f = open("abcd.txt", "r")
print(f.read())

#___________________________________

with open("text2.txt", "w") as f:
    for i in range(1,51):
        f.write(str(i) + "\n")

#__________________________________

with open("text2.txt", "r") as f:
    l = f.readlines()
    for i in l:
        print(i)
#___________________________________

with open("text2.txt", "r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

#________________________________

with open("text2.txt", "a") as f:
    for i in range(51,100):
        f.write(str(i) + "\n")
print("Done :D")

#________________________________

with open("text2.txt", "r") as f:
    l = f.readlines()
    for i in l:
        print(i)
print(l)
#________________________________

'''
Exception handling:-
Try:
except:
else:
finally:
'''

#________________________________

try:
    print(a)
except NameError:
    print("Name 'a' is not defined")
except:
    print("Error")
finally:
    print("you can't stop me from executing.")

#________________________________

try:
    f = open("text2.txt")
    try:
        f.write("hello class")
    except:
        print("Error during writing")
    finally:
        f.close()
except:
    print("Error in opening")

#____________________________________

try:
    print("hello class")
except:
    print("error")
else:
    print("working")

#____________________________________

f1 = open("cs.jpg", "rb")
f2 = open("abc.jpg", "wb+")
for x in f1:
    f2.write(x)

#____________________________________

