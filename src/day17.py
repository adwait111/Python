# string
x = "hello"
y = "suvarna"
print(x)
print(y)

print('The quote is "Try try but do not cry" ')
print("This is suvarna's book")

a = """
  I am learning javascript and python
  I find them 90% similar
  "hello"
  'bye'
"""
b = """
I am learning javascript and python
  I find them 90% similar
  "hello"
  'bye'
"""
# learning
"""
  This is multiline comment
"""
# program 2

# string store the value by index
first_name = "suvarna"
print(first_name)
print(type(first_name))
print(first_name[0])

last_name = "chaskar"
#  0  1  2  3  4  5
#  c  h  a  s  k  r
# -6 -5 -4 -3 -2  -1

print(last_name[0])
print(last_name[-1])

# for loop
# range
for i in range(len(last_name)):
    #print(i)
    print(last_name[i])

# without range
for char in first_name:
    print(char)

# while

i1 = 0
while(i1 < len(last_name)):
    #print(i1)
    print(last_name[i1])
    i1 = i1 + 1

# -------------methods------------
# program 1
first_name = "suvarna"
print(type(first_name))
fn = first_name.upper()
print(fn)

# program 2
lastName = "CHASKAR"
ln = lastName.lower()
print(ln)

# Slicing
# program 3

city = "chandrapur"
# 0  1  2  3  4  5  6  7  8  9
# c  h  a  n  d  r  a  p  u  r
#-10-9 -8 -7 -6 -5 -4 -3 -2 -1
# not included last index
print(city[1:])
print(city[3:9])
print(city[3:-2])
print(city[-7:7])
print(city[:7])
print(city[:-7])
print(city[-10 :-7])
print(city[-1 :-3])

# 0  1  2  3  4  5  6  7  8  9
# c  h  a  n  d  r  a  p  u  r
#-10-9 -8 -7 -6 -5 -4 -3 -2 -1

print(city[0:9:1])
print(city[::1])

# program 4
city2 = "apple"
q1 = city2.count("p")
print(q1)

city3 = "chandrapura"
q2 = city3.count("a")
#print(q2)

q3 = city3.count("a",4,8)
print(q3)

# program 5
city5 = "wardha"
q4 = city5.capitalize()
print(q4)

# program 6
info = "suvarnarahane9527335021"
email = "suvarnarahane@gmail.com"
q5 = info.split("a")
print(q5)
q6 = email.split("@")
print(q6)
username = q6[0]
print(username)