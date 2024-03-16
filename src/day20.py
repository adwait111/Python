g = {11,22,33,44,55,66,77,88,77}
print(type(g))

# set store the value by index???

# print(g[0])
print(g)
#string  list tuple dictionary set
# len()
# del      is common all datatype
# looping over set
for item in g:
    print(item)

# len of set
print(len(g))

# adding element to set
setB = {"amol","aditi","ram","sham"}
setB.add('satish')
print(setB)

# update the value of set
setB.update({'ramesh','suresh'})
print(setB)

# deleting set value
setB.remove("ramesh")
print(setB)

setC = {11,22,33,44}
setC.add(1)
setC.update({477,66})
setC.remove(477)
print(setC)


setD = {"pune","mumbai","banglore","kolkata"}
setD.pop()
print(setD)

setD.clear()
print(setD)

setE = {11,22,33}
setF = setE
setF.add(55)
print(setE)


setE = {11,22,33}
setF = setE.copy()
setF.add(55)
print(setE)
print(setF)