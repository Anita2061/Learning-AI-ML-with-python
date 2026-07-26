#args (positional arguments)
# (it collect as the value as tuple)

# def add(a,b,c):
#     return a + b + c
# print(add(10,20,30))


# def add(*numbers):
#     return sum(numbers)
# print(add(10,20,30))


# def fruits(*items):
#     print (items)
# fruits("apple", "banana", "orange")


#looping in function
# def display(*args):
#     for value in args:
#         print (value)
        
# display(10,20,30,40,50)    


#function to add unlimited numbers
# def add(*numbers):
#     total = 0
#     for num in numbers:
        
#         total += num
#     return total   
# print(add(10,20,30))


#real world example
# def shopping_cart(*items):
#     print("purchased items are:")
#     for items in items:
#         print(items)
   
  
# shopping_cart("bags", "dress", "grocery")       



#kwargs (keyword argument)
# it stores values in dictionary

# def student(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])
#     print(kwargs["city"])
# student(name = "Anita", age = 21, city = "Butwal")    

# output:
#   Anita
#   21
#   Butwal

def students(**kwargs):
    for key, value in kwargs.items():
        print(key,"=", value)
        
students(name = "Anita", age = 21, city = "Butwal")   
        
# output:
# name = Anita
# age = 21
# city = Butwal        


def employee(**details):
    for key, value in details.items():
        print(key, "=", value)
        
employee(Name="Diwash", Department="Operation Management", Salary=50000, country="Nepal")        

# output:
# Name = Diwash
# Department = Operation Management
# Salary = 50000
# country = Nepal

# use **kwargs when you need to accept an unkniwn number of named value.
#    eg: detail user information