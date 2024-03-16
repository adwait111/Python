# string as a parameter and string as a return type
def greet(name):
    return "hello"+" "+ name
q1 = greet("suvarna")
print(q1)

#list as a parameter ang return type
city = ["pune","mumbai","banglore","kolkata"]
def addCity(lst):
    lst.append("nagpur")
    return lst
q2 = addCity(city)
print(q2)

# dictionary as a parameter and return type
info = {
    "firstName":"suvarna",
    "lastName":"chaskar"
}
def addLanguage(information):
    information.update({"language":"marathi"})
    return information
q3 = addLanguage(info)
print(q3)

# tuple as a parameter and return type
names = ("suvarna","ninad","ramesh","suresh")
def addElement(nm):
    nm = list(nm)
    nm.append("mona")
    nm = tuple(nm)
    return nm
q4 = addElement(names)
print(q4)

# set as a parameter and return type
set = {11,22,33,44,55}
def addset(setAdd):
    setAdd.add(65)
    return setAdd
q5 = addset(set)
print(q5)

def add(x,y):
    return x + y
q1 = add(12,3)
print(q1)

add = lambda x,y:x+y
print(add)
q2 = add(23,4)
print(q2)


# function as a parameter
sub = lambda x,y:x-y
def subtraction(fn,x,y):
    # fn = lambda x,y:x-y
    q3 = fn(x,y)
    return q3

q4 = subtraction(sub,10,5)
print(q4)


