#program 1

first_name = "suvarna"
print(type(first_name))
fn = first_name.upper()
print(fn)

# program 2
last_name = "CHASKAR"
ln = last_name.lower()
print(ln)

#program 3
# slicing
city = "chandrapur"
# 0  1  2  3  4  5  6  7  8  9
# c  h  a  n  d  r  a  p  u  r
#-10-9 -8 -7 -6 -5 -4 -3 -2 -1

print(city [1:])
print(city[3:9])
print(city[3:-2])
print(city[-7:7])
print(city[:7])

# program 4
city2 = "apple"
q1 = city2.count("p")
print(q1)

city3 = "chandrapur"
q2 = city3.count("a",4)
print(q2)

# program 5
city4 = "wardha"
q3 = city4.capitalize()
print(q3)

# program 6
info = " suvarna chaskar 9527335021"
email = "suvarnarahane111@gmail.com"

q4 = info.split("1")
print(q4)

q5 = email.split('@')
print(q5)
username = q5[0]
print(username)

# program 7
str1 = "suvarna"
str2 = "chaskar"
print(str1 + str2)

# program 8
name = "suvarna rahane"
age = 27
# my name is suvarna rahane ane age is 27
uinfo = "My name is {} and age is {}".format(name,age)
print(uinfo)

print(f"My name is {name} and age is {age}")

# program 9

fruit = "papaya"
info6 = fruit.endswith("ya")
print(info6)

info7 = fruit.endswith("a")
print(info7)

# program 10
fruit = "apple"
info4 = fruit.startswith("a")
print(info4)

# program 11
info2 = "i am learning javascript"
info3 = info2.replace("javascript","python")
print(info2)
print(info3)

# program 12

city = " goa "
print(len(city))
print(len(city.strip()))

info8 = city.lstrip()
x = len(info8)
print(x)

info9 = city.rstrip()
y = len(info9)
print(y)

# program 13
               #         0   1  2  3
city = "pune"  #         p   u  n  e
print(city.index("n"))

# program 14
listA = [11,22,33,44,55.66]
listA[0] = 111
print(listA)

# program 15

info9 = "suvarna".isalpha()
print(info9)

info10 = "123654893".isdigit()
print(info10)

print("32423@".isalnum())