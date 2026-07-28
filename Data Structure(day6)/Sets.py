#sets- donot accept duplicacy

my_set= {"banana","mango","cherry"}
print (my_set)

my_set= {"banana","apple","mango"}
my_set.add("orange")
my_set.remove("apple")
my_set.add("mango")
print(my_set)


set1= {"A","B", "C"}
set2= {"B","C","D"}

a= set1.intersection(set2)
b=set2.union(set1)
print(a)
print(b)
c= set1.difference(set2)
print (c)


n:set[int]={}  #initializing empty sets
print(n)