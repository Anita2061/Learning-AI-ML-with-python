import matplotlib.pyplot as plt

marks= [88,20,79,38,90,95,87,91,12,89,25,78,82,35,86,80,83,81,77,76]
plt.hist(marks, bins=[0,20,40,60,80,100], edgecolor="black")
plt.title("distributed marks")
plt.xlabel("marks")
plt.ylabel("frequency")
plt.show()



