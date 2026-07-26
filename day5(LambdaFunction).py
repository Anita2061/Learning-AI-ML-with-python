# A lambda function is a one-line of function without a name.
# Anonymous short function

#without using lambda function
def square(x):
    return x*x
print(square(5))


#using lambda function
square = lambda x:x*x
print(square(5))