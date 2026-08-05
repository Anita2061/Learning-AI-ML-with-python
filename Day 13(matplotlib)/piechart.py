import matplotlib.pyplot as plt

expense=[2000, 5000, 1000, 3500, 6000]
categories=["rent", "food", "clothes", "misc", "gas"]
plt.pie(expense, labels=categories, autopct="%1.1f%%")
plt.title("monthly expense")
plt.show()