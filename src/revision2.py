
x = 10
print(x)
x = 1000
print(x)

# Arithematic operation
# +,-,*,/,%
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

s = 8
t = 4
print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)

# function

# function without parameter and without return type
def add():
    print(9+9)
add()
add()
add()

# function withpara and without return type
def add(x,y):
    print(x+y)
add(12,4)
add(10,5)
add(9,3)
# function with para with return type
def addC(x,y):
    return x + y
q1=addC(12,5)
print(q1)
print(q1+3)
print(q1+1)
print(q1+2)

# comparison operator
# < , > ,== , != , <= ,>=  =====>

print(2 > 1)
print(2 < 1)
print(2 == 1)
print(2 != 1)
print(2 >= 1)
print(2 <= 1)
print(2 <= 2)
print(2 >= 2)

# logical operator
# and , or , not
# and
# True   and    True    =======> True
# False  and    True    =======> False
# True   and    False   ========> False
# False  and    False   ========> False

print(2 == 2  and 3 == 3)
print(2 != 2  and 3 == 3)
print(2 == 2  and 3 != 3)
print(2 != 2  and 3 != 3)


# or
# True   and    True    =======> True
# False  and    True    =======> True
# True   and    False   ========> True
# False  and    False   ========> False

print(4 == 4 or 5 == 5)
print(4 != 4 or 5 == 5)
print(4 == 4 or 5 != 5)
print(4 != 4 or 5 != 5)

# not
# not false ====> True
# not True =====> false

print(not 4 == 4)
print(not 8 != 8)
