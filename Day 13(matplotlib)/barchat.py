import matplotlib.pyplot as plt

product = ["laptop", "smartphone", "tablet", "headphone", "smartwatch"]
sales = [800, 550, 250, 200, 500]
plt.bar(product, sales, color="blue", edgecolor="black", width=0.6)
for i, value in enumerate(sales):
    plt.text(i, value,str(value), ha= "center", va= "bottom", fontsize=10)
plt.title("product sales")
plt.xlabel("product")
plt.ylabel("number of sales")
plt.grid  #(axis='x', linestyle="--")
plt.show()



