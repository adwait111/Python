
#students = ["student1","student2","student3","student4"]
marks = [11,22,33,44,55,66,77,88,99,00]
info = ["suvarna","chaskar",23,True]

# program 1
students =[ {
    "firstName":"suvarna",
    "lastName":"chaskar",
    "age":27,
    "city":"pune",
    "skills":["python","html","css"]
  },
  {
    "firstName": "sarika",
    "lastName": "pansare",
    "age": 22,
    "city": "mumbai",
    "skills": ["djnago", "tosca", "css", "javascript"]

  },
  {
      "firstName": "amol",
      "lastName": "rao",
      "age": 23,
      "city": "nagpur",
      "skills": ["sql", "powerBI"]
  }
]

# program 1
# name:numberofskills

for student in students:
    #print(student)
    print(student['firstName'],len(student['skills']))


# program 2
# name of person living at pune
for student in students:
    if(student['city']=="pune"):
        print(student['firstName'])

# program 3
# add a property

for student in students:
    student.update({"institude":"minskole"})
    print(student)


# program 4
# add the skill of every user- "prompt enginnering"
for student in students:
    student['skills'].append('prompt enginner')
    print(students)

# program 5
# average age of all students
totalAge = 0
for student in students:
    totalAge = totalAge + student['age']
    print(totalAge/len(students))

# program 6
# name of person with python skills
for student in students:
    if "python" in student['skills']:
        print(student['firstName'])