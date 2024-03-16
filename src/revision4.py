print(1)
print(2)
print(3)
print(4)
print(5)

# for loop
# range (startIndex , endIndex(not included).steps)

for x in range(10):#by default startIndex is zero
    print(x)

for x in range(1,10):
    print(x)

for x in range(1,10,1):
    print(x)

for x in range(2,21,20):
    print(x)

for x in range(50,0,-5):
    print(x)

for x in range(30,0,-3):
    print(x)
#break
for x in range(1,9):
    if x == 5:
        break
    print(x)#0 1 2 3 4

for x in range(2,21,2):
    print(x)
    if x==10:
     break

#continue

for x in range(1,10):
    if x == 3:
        continue
    print(x)

for x in range(1,10,2):
    if x == 30:
        continue
    print(x)

# while loop

# initialization
# while condition
     # statments
     # increment/decrement
# program 1
t1 = 1
while t1 <= 3:
    print(t1)
    t1 = t1 + 1

# program 2
# print 1 to 5
t2 = 1
while t2 >= 5:
    print(t2)
    t2 = t2 + 1

#program 3
#print 5 to 1

t3 = 5
while t3 >= 1:
    print(t3)
    t3 = t3 - 1

# program 4
# table of 2
t4 = 2
while t4 <= 20:
    print(t4)
    t4 = t4 + 2

# program 5
# table 5 is reverse
t5 = 50
while t5 >= 5:
    print(t5)
    t5 = t5 - 5

# break with while loop

t6 = 1
while t6 <= 5:
    print(t6)
    if t6 == 3:
        break
    t6 = t6 + 1

t7 = 5
while t7 >= 1:
    if t7 == 3:
        break
    t7 = t7 -1
    print(t7)

t8 = 10
while t8 >= 5:
    if t8 == 7:
       t8 = t8 -1
       continue
    print(t8)
    t8 = t8 -1
