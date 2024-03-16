import re
# program 1
# search
str = 'cat man sun mpo run mat mm6 sun'
# \w = [ A - Z , a - z, 0 - 9 ]
q = re.search(r'm\w\w',str)

f = re.search(r'\wun',str)

if q:
    print(q.group())
else:
    print("match not found !")

if f:
    print(f.group())
else:
    print("match not found")

# program 2
# findall
strB = 'man,sun,mop,run,mat,fat,cat,sat'
q1 = re.search(r'\w\wp',strB)
if q1:
    print(q1.group())
else:
    print('match not found')

q2 = re.findall(r'm\w\w',strB)
q3 = re.findall(r'\wat',strB)
print(q2)
print(q3)

# program 3
# match
strC = "mon tue wed thu fri sat"
# \W = non alphanumeric
q4 = re.match(r'm\w\w',strC)
print(q4)
if q4:
    print(q4.group())
else:
    print("match not found")

# program 4
# sub()
strE = "I am learning javascript"
q5 = re.sub(r'javascript','python',strE)
print(q5)


# program 5
# split
strD = "This; is the 'core' python's book"
# \w == [A-Z , a-z,0-9]
# \W == non alpha-number
q6 = re.split(r"\W+",strD)
print(q6)
# '\W' - non alpha - number
info = 'suvarna:9527115021'
print(re.split(r'\W+',info))

# program 6
# # [A-Z , a-z , 0-9] // alphanumric  // " ", %%%
# # [/W] --- " " and special symbol
# # [/w]* zero or more repetitions
# # \d  -- represents only digits
# # \b -- only blank space

str6 = "an apple a day keeps doctor away"
e2 = re.findall(r'\ba[\w]*',str6)
print(e2)
# program 7
str7 = "The meeting will be conducted on 1st and 21st of each month"
e3 = re.findall(r'\d[\w]',str7)
print(e3)

# program 8
str8 = "one two three four five six seven 8 9 10"
e4 = re.findall(r'\b\w\w\w\w\w',str8)
print(e4)

e4 = re.search(r'\b\w{5}',str8)
print(e4.group())

# program 9
str9 = "one two three four five six seven nineteen 8 9 10"
e5 = re.findall(r'\b\w{4,}',str9)
print(e5)

# program 10
"one two three four five six seven nineteen 8 9 10"
e6 = re.findall(r'\b\w{3,5}\b',str9)
print(e6)

# program 11
str6 = "one two three four five six seven nineteen 8 9 10"
e7 = re.findall(r'\b\d{1,}\b',str6)
print(e7)
e8 = re.findall(r'\b\d+\b',str6)
print(e8)

# program 12
# a regular expression to find last word starting with 's'
# a regular expression to find last word starting with 'o'
str6 = "one two three four five six seven"
# '\Z' 0 end of string
#  \A start of string

e9 = re.findall(r'\bs[\w]*\Z',str6)
print(e9)


e10 = re.findall(r'\A\bo[\w]*',str6)
print(e10)



# program 1
str = "suvarna chaskar:9527335021"
print(str)
e = re.search(r'\d+',str)
print(e.group())

#  '\w'  --> [A-Z a-z  0-9]
#   '\W' --> Non alphanumeric
#   '\d' --> digit
#   '\D' --> non-digit

e = re.search(r'\D+',str)
print(e.group())

f = re.search(r'[\w]*[\w]*',str)
if f:
    print(f.group())
else:
    print("pattern not found")

# program 2
str = "suvarna 13-09-1996 monika 11-05-1999 amol 29-12-2000"
f = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(f)

# program 3
str = "anil akhil ajay arun arti ankur arundhati abhijeet"
g = re.findall(r'\ba[nkr][\w]*',str)
print(g)

# program 4
str = "hello world"
g = re.search(r'^he',str)
print(g.group())

# program 5
str = "hello world"
g = re.search(r'world$',str)
print(g.group())

#program 6
str  = "hello World"
g = re.search(r'world$',str,re.IGNORECASE)
print(g.group())

# program 7
students = "I got 80 marks I got 100 marks"
print(re.findall(r'\d{2,3}',students))

# program 8
student = "Amol got 80 marks Mayuri got 100 marks"
f = re.findall(r'[A-Z][a-z]*',student)
print(f)

# program 9

str = "The morning meeting will be scheduled at or 9am .evening at 8pm or 9pm"
f = re.findall(r'\d[a-z]*',str)
print(f)