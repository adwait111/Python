#Dictionary
info = ["suvarna","chaskar",23,65]
info2 = {
    "firstName":"suvarna",
    "lastName":"chaskar",
    "age":27,
    "skill":["python","django","javascript"]
}
print((info2))
print(type(info2))
# Dictionary does not stoare value by index
#print(info2[0])
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
# del info2
print(len(info2))

#dictionary
Vehicle = {
    "color":"red",
    "type":"sedane",
    "regno":123
}
# get()
print(Vehicle.get('regno'))
#print(Vehicle.get('regnoo'))

#program 2
# pop()
Vehicle = {
    "color":"red",
    "type":"sedane",
    "regno":123
}
Vehicle.pop('color')
print(Vehicle)


# program 3
# clear()
Vehicle.clear()
print(Vehicle)

# program 4
student = {
    "firstName":"suvarna",
    "lastName":"chaskar",
    "age":27,
    "skill":["python","django","javascript"]
}

print(student)
print(type(student))
print("age" in student)# bollean value

print(student.keys())

for key in student.keys():
    print(key)

for val in student.values():
    print(val)

for k,v in student.items():
    print(k,v)

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
