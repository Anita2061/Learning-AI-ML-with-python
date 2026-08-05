import matplotlib.pyplot as plt

hours =[1,2,3,4,5]
marks=[40, 45, 50, 60, 70]

plt.scatter(hours, marks)
plt.title("hours vs marks")
plt.xlabel("hours studied")
plt.ylabel("marks obtained ")
plt.show()