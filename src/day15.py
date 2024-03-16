dict = {
    "firstName":"suvarna",
    "lastName":"chaskar",
    "email":"suvarnarahane111@gmail.com",
    "rollNo":24
}
dict2 = dict
dict2["rollNo"] = 36
print(dict2)
print(dict)

dict3 = {
    "firstName":"suvarna",
    "lastName":"rahane"
}

# program 1
# copy()
dict4 = dict3.copy()
dict4['lastName']= "chaskar"
print(dict4)
print(dict3)

# program 2
# update ()
info1 = {
    "color":"blue",
    "model":"q4"
}
info2 = {
    "regNo":123
}

info1.update(info2)
print(info1)
print(info2)

# program 3
# popitem() # delete last element
info3 = {
    "color":"blue",
    "mobileNumber":213,
    "city":"pune"
}
info3.popitem()
print(info3)

# program 4
#setdefault("city","321")

info4= {
    "city":134,
    "district":34,
    "state":2
}
info4.setdefault("city","345")
print(info4)

# program 5
prop = ["fn","ln","age"]
info5 = dict.fromkeys(prop,0)
print(info5)