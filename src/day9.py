names = ["suvarna","sam","sarika"]

print(names)
names2 = names
print(names2)

names2[1] = "sameer"
print(names)
print(names2)

# remove()
cities = ["mumbai","banglore","kolkata"]
cities.remove("mumbai")
print(cities)

# pop()

cities2 =["mumbai","banglore","kolkata"]
cities2.pop()
print(cities2)

# clear()
cities.clear()
print(cities)

#index()
#            0       1       2         3       4       5      6         7
fruits = ["apple","mango","banana","papaya","apple","mango","grapes","apple"]
q111 = fruits.index("apple",1,5)
q11 = fruits.index("apple")
q1 = fruits.index("apple",2)
print(q1)
print(q11)
print(q111)

#reverse()
cities = ["goa","nagpur","wardha","chennai","pune"]
cities.reverse()
print(cities)

# sort()
cities.sort()
print(cities)

#append()

country = ["india","bangladesh","srilanka","cuba"]
country.append("pakistan")
print(country)

# insert()
country.insert(2,"china")
print(country)

# extend()

numberA = [11,22,33]
numberB = [44,55,66]

numberB.extend(numberA)
print(numberA)
print(numberB)

# count()

animals = ["dog","lion","tiger","rabbit","snake","dog"]
q22 = animals.count("dog")
print(q22)


h = [11,22,33]
j = h.copy()
j[0] = 111
print(j)
print(h)

# program 1
names = ["deepak","sameer","sham"]
names.pop()
names.pop(1)
print(names)

# program 2
numberB = [44,55,66]
numberC = numberB
numberB[0] = 999
print(numberB)
print(numberC)

# program 3
numberV = [11,22,33]
numberT = numberV.copy()
numberT[1] = 1111
print(numberV)
print(numberT)

# program 4
g = [11,22,33]
h = [44,55,66]
g.extend(h)
print(g)
print(h)

# program 5
j = ["pune","mumbai","nashik","wardha"]
j.insert(2,"goa")
print(j)

# program 6
fruits = ["mango","apple","chikoo"]
fruits.append("papaya")
print(fruits)

# program 7
fruits.sort()
print(fruits)

# program 8
fruits.reverse()
print(fruits)

# program 9


numbers = [11,22,33,44,55,44,66]
q2 = numbers.count(44)
print(q2)

for x in range(len(numbers)):
    print(x)
    print(numbers[x])