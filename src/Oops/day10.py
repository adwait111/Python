# program 1
# class Employee:
#     def __init__(self,fn,ln,adharNo):
#         # instance properties
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
#
#     # Instance method
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
#     def changeAdhar(self,change):
#         self.adharNo = change
#
# amol = Employee("amit","rao","123")
# amol.changeAdhar("23432")


# program 2
class Employee:
    country  = "India"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    @classmethod
    def changeCountry(cls):
        cls.country = "Bharat"

    def displayName(self):
        print(self.firstName + self.lastName)

amol  = Employee("amol","rao")
print(amol.firstName)
print(amol.lastName)
print(amol.country)
amol.displayName()

suvarna  = Employee("chinmay","deshpande")

print(suvarna.firstName)
print(suvarna.lastName)
print(suvarna.country)
suvarna.displayName()

suvarna.country = "Bharat India"
print(suvarna.country) # Bharat
print(amol.country) # India

Employee.changeCountry()
print(suvarna.country)
print(amol.country)

# number of Objects

class Myclass:
    n = 0
    def __init__(self):
        Myclass.n = Myclass.n + 1

    @staticmethod
    def noObject():
        print(Myclass.n)

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj4 = Myclass()

Myclass.noObject()