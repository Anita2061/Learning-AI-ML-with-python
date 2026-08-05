# (Assignment/Matplotlib.py)
# you are working as a data analyst for a retail company. the company wants to visualize its sales performance. use the following data:
    
# months=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
# sales_2024=[1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3500, 3700, 4000, 4200]
# sales_2025=[1600, 1900, 2100, 2300, 2600, 2800, 3100, 3300, 3600, 3800, 4100, 4300]
# products=["laptop", "smartphone", "tablet", "headphone", "smartwatch"]

# task:
#     1. basic line chart.
#     2. multi-line chart.
#     3. verticalbar chart.
#     4. horizontal bar chart.
#     5. histogram. 



# 1. Basic Line Chart:

import matplotlib.pyplot as plt

# months=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
# sales_2024=[1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3500, 3700, 4000, 4200]
# plt.plot(months, sales_2024, marker="o", color="blue")
# plt.title("Monthly Sales 2024")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()
       
       
# 2. Multi-Line Chart:

# import matplotlib.pyplot as plt

# months=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
# sales_2024=[1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3500, 3700, 4000, 4200]
# sales_2025=[1600, 1900, 2100, 2300, 2600, 2800, 3100, 3300, 3600, 3800, 4100, 4300]
# plt.plot(months, sales_2024, marker="o", color="blue")
# plt.plot(months, sales_2025, marker="s", color="red")
# plt.title("Monthly Sales 2024 vs 2025")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.legend(["2024", "2025"])
# plt.show()
       
       

# 3. Vertical Bar Chart:
    
import matplotlib.pyplot as plt

months=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
sales_2024=[1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3500, 3700, 4000, 4200]
sales_2025=[1600, 1900, 2100, 2300, 2600, 2800, 3100, 3300, 3600, 3800, 4100, 4300]
plt.bar(months, sales_2024, color="blue", label="2024")
plt.bar(months, sales_2025, color="red", label="2025")
plt.title("Monthly Sales 2024 vs 2025")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()
