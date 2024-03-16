# program 1
#
birthYear = [1989,1990,1991,1992]
ages = []

for x in range(len(birthYear)):
    # print(x)
    # print(birthYear[x])
    # print(2023 - birthYear[x])
    x = 2023 - birthYear[x]
    ages.append(x)
    print(ages)

# program 2
marks = [34,55,66,7,2,44,55,66,77]
above50 = []
for item in marks:
    #print(item)
    if item > 50:
        #print(item)
        above50.append(item)
        print(above50)


# program 3
totals = [11,22,33]
sum = 0
for item in totals:
    sum = sum + item
print(sum)

# program 4
cities = ["pune","banglore","kolkata"]
for item in cities:
    print("welcome" + " " +item )

