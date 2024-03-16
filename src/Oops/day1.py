# program 1
class Person:
    firstName = None
    lastName = None
    age = None
    rollNo = None
    def displayName(self):
        print(self.firstName + self.lastName)
amol = Person()
print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)
#amol.displayName()

amol.firstName = "amol"
amol.lastName = "rahane"
amol.age = 23
amol.rollNo = 45

print(amol.firstName)
print(amol.lastName)
print(amol.age)
print(amol.rollNo)
amol.displayName()

# program 2
class PersonB:
    def __init__(self,fn,ln,ag,roll):
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        self.rollNo = roll

    def displayName(self):
        print(self.firstName  + self.lastName)


amolB = PersonB("amolR","rahaneA",32,52)
suvarnaA = PersonB("suvarnaA","chaskar",96,36)

print(amolB)
print(suvarnaA)
