# Read File

file= open("fruits.txt","r")
content= file.read()
print (content)
file.close()

#output:
# Apple
# Banana
# Organge
# Grapes
# Guava


file= open("fruits.txt","r")
for line in file:
  print (line.strip())
file.close()


# Write File

file = open("students.txt","w")
file.write ("ram\n")
file.write ("sita\n")
file.write ("hari\n")
file.close()

print("file created")

#file created
# ram
# sita
# hari


#Append File

file = open("students.txt","a")
file.write ("anita\n")
file.close()

print("file updated")

# #file created
# ram
# sita
# hari


import csv
with open("Student.csv","r") as file:
  reader = csv.reader(file)
  
  for row in reader:
    print(row)
    
# output:
# ['Name', ' Math', ' English', ' Science']
# ['Ram', ' 80', ' 90', ' 95']
# ['Sita', ' 60', ' 70', ' 80']
# ['Hari', ' 50', ' 60', ' 70']


import csv
with open("student.csv","r") as file:
  reader= csv.reader(file)
  next (reader) #heading escape
  for row in reader:
    name = row[0]
    maths = int(row[1])
    english = int(row[2])
    social = int(row[3])
    average = (maths+english+social)/3
    print(name, average)
