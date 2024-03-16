# program
class Calculator:
    # class level variable
    c = 10
    def __init__(self,x,y,z):

        # instance varialbe
        self.x = x
        self.y = y
        self.z = z

amol = Calculator(122,133,144)
suvarna = Calculator(121,131,141)
print(amol.x)
print(amol.y)
print(amol.z)
print(amol.c)

print(suvarna)
print(suvarna.x)
print(suvarna.y)
print(suvarna.z)
print(suvarna.c)

suvarna.c = 99

print(amol.c)
print(suvarna.c)


# program 2 changing value of instance level variable

class CalculatorB:
    a = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # instance level method
    def changeX(self,change):
        self.x = change

SUVARNA = CalculatorB(12,3)
print(SUVARNA.x)
print(SUVARNA.y)
SUVARNA.changeX(45)
print(SUVARNA.x)

class CalculatorC:
    c = 10
    def __init__(self ,x,y):
        self.x = x
        self.y = y

    @classmethod
    def changeC(cls,ch):
        cls.c = ch
sona = CalculatorC(3,4)
print(sona.x)
print(sona.y)
print(sona.c)
amolR = CalculatorC(13,14)
print(amolR.x)
print(amolR.y)
print(amolR.c)
CalculatorC.changeC(45)
print(sona.c)
print(amolR.c)

sona.c = 99
print(amolR.c)
print(sona.c)
