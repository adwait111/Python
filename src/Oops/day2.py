class Student:
    def __init__(self,fn,ln,adhar):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adhar
    def displayName(self):
        print(self.firstName + self.lastName)

amol = Student("amol","rahane","541255")
print(amol.firstName)
print(amol.lastName)
print(amol.adharNo)

class Teacher:
    def __init__(self, fn, ln, adhar,salary):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adhar
        self.salary = salary

    def displayName(self):
        print(self.firstName + self.lastName)

    def displaySalary(self):
        print(self.salary)

amolS = Teacher("amolR","rahaneR",23,45000)

# program 1

class Student:
    def __init__(self,fn,ln,adharNO):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNO
    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):

    salary = 10000
    def displaySalary(self):
        print(self.salary)

amolT = Teacher("amolR","rahaneT",4545)
print(amolT.firstName)
print(amolT.lastName)
print(amolT.adharNo)
print(amolT.salary)
amolT.displaySalary()
amolT.displayName()

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
    def  displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)
        self.sname =  ssn
    def displaySName(self):
        print(self.sname + self.lastName)

suvarna = Son("chandrabhan","rahane","ashok","amol")
print(suvarna.firstName)
print(suvarna.lastName)
print(suvarna.fname)
print(suvarna.sname)

suvarna.displayGName()
suvarna.displayFName()
suvarna.displaySName()



