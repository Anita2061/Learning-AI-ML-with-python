# A lambda function is a one-line of function without a name.
# Anonymous short function

#without using lambda function
def square(x):
    return x*x
print(square(5))


#using lambda function
square = lambda x:x*x
print(square(5))


def calculate_salary(hours,rate):
    salary = hours * rate
    tax = salary * 0.1
    final_salary = salary - tax
    return final_salary   
print(calculate_salary(200,300))



#sorting the data using lamda
student =[
    ("ram", 78),
    ("hari", 92),
    ("sita", 60)
]

student.sort(key=lambda student:student[1])
print(student)

# output:
#     [('sita', 60), ('ram', 78), ('hari', 92)]


# lambda with map()

# add bonus marks 5 to all
marks = [50,60,0,80]

new_marks = []
for mark in marks:
    new_marks.append(mark+5)
print(new_marks)    
    
new_marks = list(map(lambda x:x+5, marks)) 
print(new_marks)   


# lambda with filter
marks = [50,60,70,90,75,80]

passed = list(filter(lambda x:x>60, marks))
print(passed)

# output:
#     [70, 90, 75, 80]


from functools import reduce
numbers = [10,20,30,40]
total = reduce(lambda x,y:x+y, numbers)

print(total)

# output:
#     100