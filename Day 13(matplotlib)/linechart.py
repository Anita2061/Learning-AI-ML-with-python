# matplotlib-> python library used for data visualization and plotting graphs, charts
# horizontal- Y 
# vertical- X


# (line chart)
import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 40, 50]
# plt.plot(x,y)
# plt.show()



months = ["jan", "feb", "mar", "apr"]
sales= [200, 250, 300, 450] 
plt.plot(months, sales, marker="o" ,color="blue")
plt.title("monthly sales") 
plt.xlabel("months") 
plt.ylabel("sales") 
# plt.grid(True) 
plt.show()    

