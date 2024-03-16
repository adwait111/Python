# tuple
# list vs Tuple
# how to create tuple
list_fruits = ["apple","mango","guava","chiku","apple","banana"]
list_num = [11,22,33,44,55,66]
list_alnum = [11,'a',22,'e',33,'i']
print(list_fruits)
print(type(list_fruits))

print(list_alnum)
print(type(list_alnum))

# tuple are immutable /unchangeable

list_num.append(66)
print(list_num)

# accessing(retrive) the element of a tuple

print(list_fruits[0])
# supported types inside a tuple

tup_one = (11,22,33,44,55)
tup_two = (11,22,33,[1,2,3,4])
tup_three = (11,22,33,[1,2,3,4,5],(2,4,6,8))
print(tup_three)

# method in tuple
print(tup_one.index(11))
print(tup_one.index(44))
print(tup_one.count(44))
print(tup_three.count(2))

print(tup_three[3][4])


tup_fruits = ('apple','mango','guava','chiku','apple','banana') #packing
print(tup_fruits[0])
print(tup_fruits[3])
print(tup_fruits[4])

a,b,c,d,e,f = tup_fruits # unpacking
print(a)
print(b)