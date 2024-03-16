# loops

#for x in range(startValue,EndValue(end value not incuded),stepsize):
# statment

# program 1

# print 0 to 5
for x in range(6):
    print(x)

#print hello 3 times
for x in range(3):
    print("hello")

#print 1 to 5
for x in range(1,6):
    print(x)

#print 5 to 1
for x in range(5,0,-1):
    print(x)

#print 5 table reverse
for x in range(50,0,-5):
    print(x)

#print table of 2
for x in range(2,21,2):
    print(x)

#break statment with for loop for
for item in range(1,5):
    if item == 3:
        break
    print(item)

for item in range(1,5):
    print(item)
    if item == 3:
        break

for item in range(5,55,5):
    if item == 45:
        break
    print(item)


for item in range(50,0,-5):
    if item == 45 :
        break
    print(item)

# continue for loop
for x in range(1,6):
    if x == 3 :
        continue
    print(x)

for x in range(20,0,-2):
    if x == 10:
        continue
    print(x)






