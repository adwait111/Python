# compile time error // missing symbols// sytax error
# runtime error
# logical error// human error for eg spelling mistake


# program 1
#  compile error
# def addition(x,y)
#     print(x+y)
# addition(12,4)

# program 2
# run time error
# x = input("enter the number one")
# y = input("enter the number two")
# print("hello")
# print(int(x)/int(y))
# print("bye")

# program 3
# logical error
# def calculatorAge(age):
#     return age
# e = calculatorAge(20)
# print(e)

# program 4
# print("hello")
# print(10 /0)
# print("bye")


print("hello")
try:
    print(10/0)
except Exception:
    print("division by zero")
print("hello")

print("--------------------")
try:
    print(10/0)
    print([11,22,33,44,5].index(67))
except Exception:
    print("hi")
except Exception:
    print("bye")
else:
    print("hello")
finally:
    print("excute all time")
