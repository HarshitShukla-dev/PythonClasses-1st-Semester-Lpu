#polymorphism
print(len("cipherschools"))
print(len([10,20,30,40]))

#________________________________

def sum(*arg):
    s = 0
    for i in arg:
        s += i    
    return s

print(sum(1,2,3,4,5,6))

#__________________________________

def sum(x,y,z=0):
    return x + y + z

print(sum(1,2,3))
print(sum(1,2))

#_____________________________________

class India:
    def capital(self):
        print("New Delhi is the capital of India")
    
    def language(self):
        print("Multiple languages are spoken in India")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA")

    def language(self):
        print("English is the primary language of USA")

obj_ind = India()
obj_USA = USA()

for country in (obj_ind,obj_USA):
    country.capital()
    country.language()

#________________________________________

class Bird:
    def intro(self):
        print("This is Bird class")

    def flight(self):
        print("Most of them can fly ")

class Parrot(Bird):
    def flight(self):
        print("Parrot can fly")                 #method overwriding

class Ostrich(Bird):
    def flight(self):
        print("Ostrich can not fly")

obj_bird = Bird()
obj_parrot = Parrot()
obj_ostrich = Ostrich()

obj_ostrich.intro()
obj_ostrich.flight()

obj_parrot.intro()
obj_parrot.flight()

obj_bird.intro()
obj_bird.flight() 

#_______________________________________________

