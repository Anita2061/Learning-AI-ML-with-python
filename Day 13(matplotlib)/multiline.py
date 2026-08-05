import matplotlib.pyplot as plt

months=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
sales_2024=[200, 250, 300, 450, 500, 600, 700, 800, 900, 1000, 1100, 1200]
sales_2025=[250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]

plt.plot(months, sales_2024, marker="o", color="blue", label="sales_2024")
plt.plot(months, sales_2025, marker="s", color="red", label="sales_2025")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.legend()
plt.show()
