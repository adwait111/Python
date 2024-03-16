# Abstract class

# class MyClass:
#     def calculatate(self,x):
#         print(x)
#
# obj = MyClass()
# obj.calculatate(1)
# obj1 = MyClass()
# obj.calculatate(2)
# obj2 = MyClass()
# obj.calculatate(3)
#
#

# cube
# squareroot
# square

from abc import ABC,abstractmethod
class myClass(ABC):
    @abstractmethod
    def Calculate(self,x):
        pass
class square(myClass):
        def Calculate(self,x):
            print('square')
class cube(myClass):
    def Calculate(self,x):
        print('cube')
class squareroot(myClass):
    def Calculate(self,x):
        print('Squareroot')

# we cannot create object of abstract class
# abstrct class can have - abstract method and non- abstractmethod
# it mandatory for class to implement abstract method if inherited

class Vehicle(ABC):
    @abstractmethod
    def wheel(self, x):
        pass
    def Country(self):
        print("India")

class Maruti(Vehicle):
    def wheel(self, x):
        print("4 wheels")


class Audi(Vehicle):
    def wheel(self, x):
        print("5 wheels")

a = Audi()
a.wheel(5)
a.Country()

b = Maruti()
b.wheel(4)
b.Country()



# a = Cube()
# b = Square()
# c = SquareRoot()

# a.Calculate(12)
# b.Calculate(34)
# c.Calculate(56)
#

