'''The company want to understand whether customer satisfaction is related to sales performance.
management wants to know:
do customers with higher satisfaction  scores tend to generate higher-value purchase?
use the "csv" dataset.
columns to use:
Customer_Satisfaction
Total_Amount 
Category
Sales_Channel
loyalty_Score

task to do:
load data
clean the data in category
clean missing values as well
create satisfaction groups(satisfaction_level: 1-2 = low, 3= medium, 5= high)
analyze sales by satisfaction label and category
plot the result 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv("Day 14/business_data_cleaning_practice_6200_rows.csv")




# Select required columns
data = df[[
    "Customer_Satisfaction",
    "Total_Amount",
    "Category",
    "Sales_Channel",
    "Loyalty_Score"
]]




# Clean Category column
data["Category"] = data["Category"].str.strip()

data["Category"] = data["Category"].replace({
    "I.T.": "IT",
    "Information Technology": "IT"
})


# Handle Missing Values
data = data.dropna()



# Create Satisfaction Groups
# 1-2 = Low
# 3 = Medium
# 5 = High
def satisfaction_level(score):
    if score <= 2:
        return "Low"
    elif score == 3:
        return "Medium"
    else:
        return "High"

data["Satisfaction_Level"] = data["Customer_Satisfaction"].apply(satisfaction_level)



# Analyze Sales by Satisfaction Level and Category
sales_analysis = data.groupby(
    ["Satisfaction_Level", "Category"]
)["Total_Amount"].sum().unstack()

print("\nSales Analysis")
print(sales_analysis)

# output:
# Sales Analysis
# Category            Electronics    Furniture            IT  Office Supplies
# Satisfaction_Level                                                         
# High                45365321.88  44491477.01  1.259982e+08      45979862.41
# Low                 23073656.62  28192099.12  8.355518e+07      31503248.45
# Medium               9300074.40  16792280.52  4.754410e+07      16854698.48    



# Highest Sales by Satisfaction Level
highest_sales = data.groupby("Satisfaction_Level")["Total_Amount"].sum()

print("\nSales by Satisfaction Level")
print(highest_sales)

# output:
# Sales by Satisfaction Level
# Satisfaction_Level
# High      2.618348e+08
# Low       1.663242e+08
# Medium    9.049115e+07
# Name: Total_Amount, dtype: float64    



# Plot
sales_analysis.plot(
    kind="bar",
    figsize=(10,6)
)

plt.title("Sales by Customer Satisfaction Level and Category")
plt.xlabel("Customer Satisfaction Level")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.legend(title="Category")
plt.tight_layout()

plt.show()

