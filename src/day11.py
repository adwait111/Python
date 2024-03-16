# list comprehension

x = [1,2,3,4,5,6,7,8,9,10]
tableOfTwo = []
for item in x:
    tableOfTwo.append(item*2)
    print(tableOfTwo)

# program 2
#[expression loop condition]
x = [1,2,3,4,5,6,7,8,9,10]
q3 = [item*2 for item in x]
print(q3)

#program 3
birthYear = [1989,1990,1991,1992]
ages = []
for x in range (len(birthYear)):
    ag = 2023 - birthYear[x]
    ages.append(ag)
    print(ages)

ages2 = [2023 - item for item in birthYear]
print(ages2)

# [expression:loop:condition]
#program 4
marks = [33,44,55,66,88,34,55,67]
above40 = []
for item in marks:
    if item > 40:
        above40.append(item)
        print(above40)

above40two = [item for item in marks if item > 40]
print(above40two)

# program 5
square = [1,2,3,4,5,6,7,8,9,10]
squares = [item*item for item in square]
print(squares)

# program 6
names = ["suvarna","monika","pooja","sarika","satish"]
capitalNames = [item.upper()for item in names]
print(capitalNames)

# program 7
numberB = [33,444,5,6]
even =["even" for item in numberB if item % 2 == 0]
print(even)

