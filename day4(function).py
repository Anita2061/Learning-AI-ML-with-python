count= 1
while count<=5:
    print("hello")
    count+=1


# even numbers
num=2
while num<=10:
    print(num)
    num+=2


num=7
num=0
while num!=unum:
    unum=int(input("enter your number: "))


i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)




# functions
def greet():
    print("hello")
greet()
    

def add(a,b):
    return a+b
print(add(5,3))

def name(misti):
    return misti
print(name("misti"))


def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("invalid discount")
    return price *(1-discount_percent/100)
print(calculate_discount(100,50))



def c_to_f(c):
    return c*1.8+32
print(c_to_f(10))
def f_to_c(f):
    return f-32/1.8
print(f_to_c(109))