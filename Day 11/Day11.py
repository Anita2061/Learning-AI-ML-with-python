import pandas as pd

df = pd.read_csv("day 11/business_data_cleaning_practice_6200_rows.csv")
# print(df.info)   #missing value
# print(df.describe)

print(df.isnull().sum())
# output:
# Customer_ID              3085
# Customer_Name               0
# Gender                    920
# Age                      2479
# Email                    2575
# Phone                    3109
# City                        0
# Province                    0
# Country                     0
# Product_ID               4122
# Product_Name                0
# Category                    0
# Brand                       0
# Unit_Price               3088
# Order_ID                 4130
# Order_Date               2036
# Quantity                    0
# Discount                    0
# Tax                         0
# Total_Amount             3143
# Payment_Method              0
# Sales_Channel               0
# Warehouse                   0
# Delivery_Status             0
# Delivery_Days            2037
# Salesperson                 0
# Region                      0
# Customer_Satisfaction     900
# Loyalty_Score            3087
# Return_Flag              1256
# dtype: int64

df["Age"] = df["Age"].fillna(df["Age"].median())
print(df.isnull().sum())
# output:
# Customer_ID              3085
# Customer_Name               0
# Gender                    920
# Age                      2479
# Email                    2575
# Phone                    3109
# City                        0
# Province                    0
# Country                     0
# Product_ID               4122
# Product_Name                0
# Category                    0
# Brand                       0
# Unit_Price               3088
# Order_ID                 4130
# Order_Date               2036
# Quantity                    0
# Discount                    0
# Tax                         0
# Total_Amount             3143
# Payment_Method              0
# Sales_Channel               0
# Warehouse                   0
# Delivery_Status             0
# Delivery_Days            2037
# Salesperson                 0
# Region                      0
# Customer_Satisfaction     900
# Loyalty_Score            3087
# Return_Flag              1256
# dtype: int64
# Customer_ID              3085
# Customer_Name               0
# Gender                    920
# Age                         0
# Email                    2575
# Phone                    3109
# City                        0
# Province                    0
# Country                     0
# Product_ID               4122
# Product_Name                0
# Category                    0
# Brand                       0
# Unit_Price               3088
# Order_ID                 4130
# Order_Date               2036
# Quantity                    0
# Discount                    0
# Tax                         0
# Total_Amount             3143
# Payment_Method              0
# Sales_Channel               0
# Warehouse                   0
# Delivery_Status             0
# Delivery_Days            2037
# Salesperson                 0
# Region                      0
# Customer_Satisfaction     900
# Loyalty_Score            3087
# Return_Flag              1256
# dtype: int64


df["Gender"] = df["Gender"].fillna(("unknown"))
print(df.isnull().sum())
# output:
# Customer_ID              3085
# Customer_Name               0
# Gender                      0
# Age                      2479
# Email                    2575
# Phone                    3109
# City                        0
# Province                    0
# Country                     0
# Product_ID               4122
# Product_Name                0
# Category                    0
# Brand                       0
# Unit_Price               3088
# Order_ID                 4130
# Order_Date               2036
# Quantity                    0
# Discount                    0
# Tax                         0
# Total_Amount             3143
# Payment_Method              0
# Sales_Channel               0
# Warehouse                   0
# Delivery_Status             0
# Delivery_Days            2037
# Salesperson                 0
# Region                      0
# Customer_Satisfaction     900
# Loyalty_Score            3087
# Return_Flag              1256
# dtype: int64


missing = df["Customer_ID"].isna()
df.loc[missing,"Customer_ID"] = [f"CUST{1000+i}" for i in range(missing.sum())]
print(df.isnull().sum())
# output:
# Customer_ID                 0
# Customer_Name               0
# Gender                    920
# Age                      2479
# Email                    2575
# Phone                    3109
# City                        0
# Province                    0
# Country                     0
# Product_ID               4122
# Product_Name                0
# Category                    0
# Brand                       0
# Unit_Price               3088
# Order_ID                 4130
# Order_Date               2036
# Quantity                    0
# Discount                    0
# Tax                         0
# Total_Amount             3143
# Payment_Method              0
# Sales_Channel               0
# Warehouse                   0
# Delivery_Status             0
# Delivery_Days            2037
# Salesperson                 0
# Region                      0
# Customer_Satisfaction     900
# Loyalty_Score            3087
# Return_Flag              1256
# dtype: int64