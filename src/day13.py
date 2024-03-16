listA =["suvarna","chaskar",45,66]
#retrive
print(listA[0])
#update
listA[1]="dani"
#add
listA.append("pune")
#delete
#del listA

# total no of element
print(len(listA))

listA = ["suvarna","chaskar",45,66]
for item in listA:
    print(item)

for item in range(len(listA)):
    print(listA[item])

#dic
info = {
        "firstName":"suvarna",
        "lastName":"chaskar",
        "age":45,
        "rollNo":66
}
# dic does not stores value by index
q2 = info['firstName']
print(q2)

# update
q3 = info['lastName']= 'Rahane'
print(q3)

# add
q4 = info['city'] = 'nashik'
print(q4)
print(info)

# delete
# del info
print(len(info))

# check whether element is present
# looping through list
cities = ["wardha","pune","nagpur"]
for item in cities:
    print(item)
print("wardha"in cities)

info2 = {
    "firstName": "suvarna",
    "lastName": "chaskar",
    "age": 27
}
print("age" in info2)
for item in info2:
   # print(item)
   print(item,info2[item])

car = {
    "color":"blue",
    "model":"Q4",
    "company":"Audi"
}
for item in car:
    print(item,car[item])

# get ()
q5 = car.get("model")
print(q5)
