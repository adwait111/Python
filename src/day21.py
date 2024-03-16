# program 1

setA = {11,22,33,44}
setA.pop()
print(setA)

# program2
setA = {11,22,33,44}
setA.update({101,102,103})
setA.update([55,66,77])
setA.update((99,88,100))
print(setA)

#program 3
setC = {11,22,33}
setD = {22,33,44}
setE = setC.intersection(setD)#SAME NUMBER
print(setE)

#program 4
setC = {11,22,33}
setD = {22,33,44}
setF = setC.union(setD)
print(setF)

# program 5
setC = {11,22,33}
setD = {22,33,44}
setC.intersection_update(setD)
print(setC)

# program 6
setC = {11,22,33}
setD = {22,33,44}
print(setC.difference(setD))
print(setC.difference(setD))

# program 7
setC = {11,22,33}
setD = {22,33,44}
setC.difference_update(setD)
print(setC)

# program 8
setC = {11,22,33}
setD = {22,33,44}
setG = setC.symmetric_difference(setD)
print(setG)
setC.symmetric_difference_update(setD)
print(setC)

# program 9
setC = {11,22}
setD = {11,22,33,44}
print(setC.issubset(setD))
print(setD.issuperset(setC))

# program 10
setC = {112,222}
setD = {11,22,33,44}
print(setC.isdisjoint(setD))

# program 11
setC = {112,333}
setD = {11,22,33,44}
setC.remove(112)
print(setC)

print(setC.discard(112))
setCities = {"pune","mumbai","banglore","kolkata"}
print(setCities)
for item in setCities:
    print(item)
