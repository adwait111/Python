
# program 1
print("Hello")
# integer
x = 10
print(x)
print(type(x))
# 10,-90,0

# program 2
# float
x1 = 10.9
print(x1)
print(type(x1))
#12.4,55.6,0.56

#program 3
# boolean
a = True
print(a)
print(type(a))
#true or false

#program 4
d = "suvarna"
print(d)
print(type(d))
# "A","a","123@sda"," "

#collection
# program 5
# string
e = "sinnar"
print(e)
print(type(e))

firstName = "SUVARNA"
# firstName.lower() # suvarna
# firstName.upper() # SUVARNA
q1 = firstName.startswith('s')
print(q1)
firstName.endswith('na')#true
firstName.rstrip()# trim rs
q2 = firstName.lstrip() # trim ls
print(q2)
q3 = firstName.capitalize()
print(q3)
q4 = firstName.count('A')
print(q4)
q5 = firstName.index('R')# find index
print(q5)
q6 = firstName.split('V')# divide into two part
print(q6)
# slicing
print(firstName[1:3])
print(firstName.replace('SUVARNA','suvarna'))
q7 = "suvarna".isalpha()
print(q7)

q8 = "123654893".isdigit()
print(q8)
print("32423@".isalnum())
for x in firstName:
    print(x)

for y in range(len(firstName)):
    print(firstName[y])

# program 6
# list (multiple element at one memory)
cities = ["pune","mumbai","banglore","kolkata","kolkata"]
print(cities)
print(type(cities))
cities.append("nashik")
cities.remove("mumbai")
print(cities)
# cities.pop()
# print(cities)
# clear()
#cities.clear()
#print(cities)
# cities.remove("mumbai")
# print(cities)
cities.reverse()
print(cities)

numbers = [11,22,33,44,55,44,66]
q2 = numbers.count(44)
print(q2)
for x in range(len(numbers)):
    print(x)
    print(numbers[x])

g = [11,22,33]
h = [44,55,66]
g.extend(h)
print(g)
print(h)

marks = [34,55,66,7,2,44,55,66,77]
above50 = []
for item in marks:
    #print(item)
    if item > 50:
        #print(item)
        above50.append(item)
        print(above50)

# dictionary
info = ["suvarna","chaskar",23,65]
info2 = {
    "firstName":"suvarna",
    "lastName":"chaskar",
    "age":27,
    "skill":["python","django","javascript"]
}

print(info)
print(info2)
# Dictionary does not stoare value by index
#retrive
q1 = info2['firstName']
print(q1)
#update
info2['firstName']= 'Monika'
print(info2)
# add
info2['city'] = 'pune'
print(info2)
# #delete

# get()
print(info2.get('lastName'))
# pop()
print(info2.pop('age'))
#clear()
print(info2.clear())
country = {
    "cities":356,
    "states":29,
    "pincode":1000

}

print(country['cities'])
for key in country:
    print(key,country[key])

for key in country.keys():
    print(key)

for val in country.values():
    print(val)

for k,v in country.items():
    print(k,v)

# # tuple(fixed length)
# students = ("ram","sham","satish","sachin")
# print(students)
# print(type(students))
# # students[4] = "Suvarnaa"
#
# marks = 8,10
# print(type(marks))
#
# # set (does not allowe duplicate value)
# names = {"suvarna","sarika","poorva","ram","suvarna"}
# print(names)
# print(type(names))
#

#
#
#
#
#
