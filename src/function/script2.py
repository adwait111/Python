# lambda

def add(x,y):
    return x + y

q1 = add(12,4)
print(q1)

addB = lambda x,y:x+y
q2 = addB(3,4)
print(q2)
q = lambda x : x*x
q3 = q(3)
print(q3)

names = ["suvarna","amol","monika","archana","kaveri"]
def changeName(lst):
    lst[0] = "sona"
    return lst

q4 = changeName(names)
print(q4)
print(names)

lstA = [1,2,3,4,5,6]
n = []
for x in lstA:
    n.append(x*3)
print(n)

# list comprehension -- o/p - list
#[expression:loop:condition]

q4 = [x*3 for x in lstA]
print(q4)

lstB = [44,55,66,77,33,44,55,66,77,11,22,33,7,8,9]
lstC = []
for x in lstB:
    if x % 2 == 0:
        lstC.append(x)
print(lstC)

#[expression:loop:condition]
q5 = [x for x in lstC if x % 2 == 0]
print(q5)