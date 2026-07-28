#assignment

def student_marksheet():
    student_name = input("Enter student name: ")

    subject1 = float(input("Enter marks in English: "))
    subject2 = float(input("Enter marks in Mathematics: "))
    subject3 = float(input("Enter marks in Science: "))
    subject4 = float(input("Enter marks in Computer: "))

    total = subject1 + subject2 + subject3 + subject4
    percentage = total / 4

    print("\nSTUDENT MARKSHEET")
    print("Student Name:", student_name)
    print("English:", subject1)
    print("Mathematics:", subject2)
    print("Science:", subject3)
    print("Computer:", subject4)
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

student_marksheet()# Calling the function


# output:
# Enter student name: Anita Gyawali
# Enter marks in English: 50
# Enter marks in Mathematics: 60
# Enter marks in Science: 70
# Enter marks in Computer: 80

# STUDENT MARKSHEET
# Student Name: Anita Gyawali
# English: 50.0
# Mathematics: 60.0
# Science: 70.0
# Computer: 80.0
# Total Marks: 260.0
# Percentage: 65.0 %