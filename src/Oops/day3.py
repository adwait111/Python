# class GrandFather:
#     def _init_(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln

#     def displayGName(self):
#         print(self.firstName + self.lastName)

# class Father(GrandFather):
#     def _init_(self, fn, ln,ffn):
#         super()._init_(fn, ln)
#         self.fname = ffn

#     def displayFName(self):
#         print(self.fname + self.lastName)

# shirish = Father("manohar","deshpande","shirish")
# print(shirish.firstName)
# print(shirish.lastName)
# print(shirish.fname)
# shirish.displayGName()
# shirish.displayFName()

# Multi-level
# class GrandFather:
#     def _init_(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln

#     def displayGName(self):
#         print(self.firstName + self.lastName)

# class Father(GrandFather):
#     def _init_(self, fn, ln,ffn):
#         super()._init_(fn, ln)
#         self.fname = ffn

#     def displayFName(self):
#         print(self.fname + self.lastName)

# class Son(Father):
#     def _init_(self, fn, ln, ffn,ssn):
#         super()._init_(fn, ln, ffn)
#         self.sname = ssn
#     def displaySName(self):
#         print(self.sname + self.lastName)

# chinmay = Son("manohar","deshpande","shirish","chinmay")

# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.sname)
# print(chinmay.fname)

# chinmay.displayFName()
# chinmay.displayGName()
# chinmay.firstName()

# program 3

# Herarchical inheritance
# class Mother:
#     def _init_(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln

#     def displayMName(self):
#         print(self.firstName + self.lastName)


# class Son(Mother):
#     def _init_(self, fn, ln , ssn):
#         super()._init_(fn, ln)
#         self.sname = ssn

#     def displaySname(self):
#         print(self.sname + self.lastName)

# class Daugher(Mother):
#     def _init_(self, fn, ln , dn):
#         super()._init_(fn, ln)
#         self.dname = dn

#     def displayDname(self):
#         print(self.dname + self.lastName)

# chinmay = Son("kanchan","deshpande","chinmay")
# gauri = Daugher("kanchan","deshpande","gauri")

# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.sname)
# chinmay.displaySname()
# chinmay.displaySname()


class Father:
    def _init_(self, fn, ln):
        print("Father constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayFName(self):
        print(self.firstName + self.lastName)


class Mother:
    def _init_(self, fn, ln):
        print("Mother constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother, Father):
    def _init_(self, fn, ln, ssn):
        super()._init_(fn, ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)


chinmayh = Son("shirish", "deshpande", "chinmay")