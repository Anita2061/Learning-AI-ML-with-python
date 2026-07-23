# logic
# today we will build simple logic in python programming


a = "fail"
if a == "pass":
  print("you will be project manager")
else:
  print("you will come for reexam")

    
    
    
a = int(input("enter your number: "))    
if a>=80:
  print("distinction")  
elif a>=50:
  print("pass")  
else:
  print("fail")      
 
 
 
 
name = str(input("enter your name: "))  
java = int(input("enter the marks of Java: "))
dsa= int(input("enter the marks of DSA: "))
ds = int(input("enter the marks of DS: "))
dl = int(input("enter the marks of DL: "))

if java<=32 & dsa<=32 & ds<=32 & dl<=32:
    print ("fail")
else:
    print("pass")
    
total =  java + dsa + ds + dl
print(total)
avg = (total/4)
print(avg)




# real world example
username = input("enter your username: ")   
password = input("enter your password: ")  

if username == "admin" and password == "password123": 
    print("you are loggedin")
else:
    print("incorrect username and password")    




year = int(input("enter the year of service: "))
rating = str(input("enter the rating: "))

if year>=5 and rating == "excellent":
    print("you will get 20% bonus")
elif year>=3 and rating == "good":
    print("you will gt 10% bonus") 
else:
    print("there is no bonus")       