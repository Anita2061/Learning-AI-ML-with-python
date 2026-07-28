# write a python program to manage the record of 3 students using a nested dictonary
# each students should have the following info:



students = {
    "S001": {
        "name": "Anita",
        "age": 21,
        "faculty": "BITM",
        "finance": 75,
        "computer": 70
    },
    "S002": {
        "name": "Diwash",
        "age": 24,
        "faculty": "BITM",
        "finance": 80,
        "computer": 92
    },
    "S003": {
        "name": "Anu",
        "age": 20,
        "faculty": "BITM",
        "finance": 72,
        "computer": 65
    }
}

#Displaying details of all students
print("Details of all students:")
for student_id, details in students.items():
    print(student_id, details)


# Displaying details of specific student S001
print("\nDetails of S001:")
print(students["S001"])


# Updating finance marks of S001 to 95
students["S001"]["finance"] = 95

print("\nAfter updating finance marks of S001:")
print(students["S001"])


# Calculating and display total marks of each student
print("\nTotal marks of each student:")

for student_id, details in students.items():
    total = details["finance"] + details["computer"]
    print(details["name"], "=", total)


# Finding and display the student with the highest total marks
highest_student = ""
highest_total = 0

for student_id, details in students.items():
    total = details["finance"] + details["computer"]

    if total > highest_total:
        highest_total = total
        highest_student = details["name"]

print("\nStudent with highest total marks:")
print(highest_student, "=", highest_total)



# output:
# Details of all students:
# S001 {'name': 'Anita', 'age': 21, 'faculty': 'BITM', 'finance': 75, 'computer': 70}
# S002 {'name': 'Diwash', 'age': 24, 'faculty': 'BITM', 'finance': 80, 'computer': 92}
# S003 {'name': 'Anu', 'age': 20, 'faculty': 'BITM', 'finance': 72, 'computer': 65}

# Details of S001:
# {'name': 'Anita', 'age': 21, 'faculty': 'BITM', 'finance': 75, 'computer': 70}

# After updating finance marks of S001:
# {'name': 'Anita', 'age': 21, 'faculty': 'BITM', 'finance': 95, 'computer': 70}

# Total marks of each student:
# Anita = 165
# Diwash = 172
# Anu = 137

# Student with highest total marks:
# Diwash = 172