# inheritance

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayM(self):
        print(self.firstName + self.lastName)

class Father:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayF(self):
        print(self.firstName + self.lastName)

class Son(Mother,Father):
    def __init__(self,fn, ln,sn):
        super().__init__(fn, ln)
        self.sname = sn

    def displayS(self):
        print(self.sname + self.lastName)

Amol = Son("ashok","chaskar","Amol")
print(Amol)
print(Amol.lastName)

# Method resolution order

class A(object):
    def method(self):
        print('A class is called')
        super().method()
class B(object):
    def method(self):
        print('B is called')
        super().method()
class C(object):
    def method(self):
        print('C is called')

class X(A,B):
    def method(self):
        print('Xis called')
        super().method()
class Y(B,C):
    def method(self):
        print('Y is called')
        super().method()
class P(X,Y,C):
    def method(self):
        print('P is called')
        super().method()


p = P()
p.method()


