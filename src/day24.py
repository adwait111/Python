
a = 100

try:
    b = 0
    c = a / b
    name = "TAVISH"
    print(c)
    print(name[1])
except ZeroDivisionError as e:
    print("Something went wrong", e)
except IndexError as e:
    print("Something went wrong", e)
else:
    print("Complete Code executed successfully")
finally:
    print("This will always be executed")
print(a)

print("Hello World")

# custom Exception
# raising  user defined Exceptions

# x = 11
# print(x%2!=0)

# if x%2!=0 :
#   raise Exception("Enter even Number Only")
# else:
#   print("Entered num is even")


current_year = 2023
year_born = 2990

# if year_born>current_year:
#   raise Exception("INVALID YEAR OF BIRHT")
# else:
#   age = current_year - year_born
#   print(age)


try:
    if year_born > current_year:
        raise Exception("INVALID YEAR OF BIRHT")
    else:
        age = current_year - year_born
        print(age)
except:
    print("Some Error Occured")