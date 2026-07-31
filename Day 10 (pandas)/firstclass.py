import pandas as pd

# (series) - A one-dimensional labeled array capable of holding any data type 
# (integers, strings, floating point numbers, Python objects, etc.)
marks = pd.Series ([80, 75, 90, 85, 95])
print(marks)

# output:
# 0    80
# 1    75
# 2    90
# 3    85
# 4    95
# dtype: int64

numbers = pd.Series ([100, 200, 300, 400, 500])
print(numbers)

# output:
# 0    100
# 1    200
# 2    300
# 3    400
# 4    500
# dtype: int64




# (Data Frame) - A two-dimensional labeled data structure with columns of potentially different types. 
# You can think of it like a spreadsheet or SQL table, or a dict of Series objects. 
# It is generally the most commonly used pandas object.

student = {
    
    'Name': ['sita', 'hari', 'gita', 'ram'],
    'Age':  [20, 21, 22, 23],
    'math': [80, 95, 75, 90]
}
df = pd.DataFrame(student)    
print(df)

# output:
#    Name  Age math
# 0  sita   20   80
# 1  hari   21   95
# 2  gita   22   75
# 3  ram   23   90  

print(df.head(2))   #first row of data
# output:
#    Name  Age  math
# 0  sita   20   80
# 1  hari   21   95

print(df.tail(3))   #last row of data
# output:
#    Name  Age math
# 1  hari   21   95
# 2  gita   22   75
# 3  ram    23   90

print(df[["Name", "Age"]])
# output:
#    Name  Age
# 0  sita   20
# 1  hari   21
# 2  gita   22
# 3  ram    23 

print(df.loc[1:3])  #from first
# output:
#    Name  Age math
# 1  hari   21   95
# 2  gita   22   75
# 3  ram    23   90

print(df.iloc[1:3])  #from last
# output:
#     Name  Age math
# 1  hari   21   95
# 2  gita   22   75

print (df.describe())
# output:
#           Age       math
# count   4.000000   4.000000
# mean   21.500000  85.000000
# std     1.290994   9.128709
# min    20.000000  75.000000
# 25%    20.750000  78.750000
# 50%    21.500000  85.000000
# 75%    22.250000  91.250000
# max    23.000000  95.000000


employe = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Ramesh", "Suresh", "Gopal", "Rohit", "Rakesh", "Sanjay"],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
}    
df = pd.DataFrame(employe)
print(df) 
# output:
#     Name Department  Salary
# 0     Ram         IT   50000
# 1    Hari         HR   60000
# 2    Sita    Finance   70000
# 3    Gita         IT   80000
# 4  Ramesh         HR   90000
# 5  Suresh    Finance  100000
# 6   Gopal         IT  110000
# 7   Rohit         HR  120000
# 8  Rakesh    Finance  130000
# 9  Sanjay         IT  140000   

print(df.shape)
# output:
# (10, 3)

print(df.columns)
# output:
#     Index(['Name', 'Department', 'Salary'], dtype='str')

print(df.dtypes)
# output:
# Name            str
# Department      str
# Salary        int64
# dtype: object

print(df.head())   #first five data
# output:
#     Name Department  Salary
# 0     Ram         IT   50000
# 1    Hari         HR   60000
# 2    Sita    Finance   70000
# 3    Gita         IT   80000
# 4  Ramesh         HR   90000

print(df.tail())   #last five data
# output:
#     Name Department  Salary
# 5  Suresh    Finance  100000
# 6   Gopal         IT  110000
# 7   Rohit         HR  120000
# 8  Rakesh    Finance  130000
# 9  Sanjay         IT  140000

print(df.info)
# output:
#     <bound method DataFrame.info of      
#       Name Department  Salary
# 0     Ram         IT   50000
# 1    Hari         HR   60000
# 2    Sita    Finance   70000
# 3    Gita         IT   80000
# 4  Ramesh         HR   90000
# 5  Suresh    Finance  100000
# 6   Gopal         IT  110000
# 7   Rohit         HR  120000
# 8  Rakesh    Finance  130000
# 9  Sanjay         IT  140000>

print(df.info())   #check the data is empty or not
# output:
#     <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 3 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   Name        10 non-null     str  
#  1   Department  10 non-null     str  
#  2   Salary      10 non-null     int64
# dtypes: int64(1), str(2)
# memory usage: 372.0 bytes
# None

print(df.describe())    #prints stats value
# output:
#            Salary
# count    10.000000
# mean    95000.000000
# std     30276.503541
# min     50000.000000
# 25%     72500.000000
# 50%     95000.000000
# 75%    117500.000000
# max    140000.000000

print(df.fillna(0, inplace = True))   #print same table
# output:
#     Name Department  Salary
# 0     Ram         IT   50000
# 1    Hari         HR   60000
# 2    Sita    Finance   70000
# 3    Gita         IT   80000
# 4  Ramesh         HR   90000
# 5  Suresh    Finance  100000
# 6   Gopal         IT  110000
# 7   Rohit         HR  120000
# 8  Rakesh    Finance  130000
# 9  Sanjay         IT  140000


employe = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Ramesh", "Suresh", "Gopal", "Rohit", "Rakesh", "Sanjay"],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Salary": [None, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
}    
df = pd.DataFrame(employe)

print(df.isnull().sum())
# output:
# Name          0
# Department    0
# Salary        1
# dtype: int64

df =df.dropna()
print(df.dropna)   #salary none vako data remove garne
# output:
#     <bound method DataFrame.dropna of     
#      Name Department    Salary
# 1    Hari         HR   60000.0
# 2    Sita    Finance   70000.0
# 3    Gita         IT   80000.0
# 4  Ramesh         HR   90000.0
# 5  Suresh    Finance  100000.0
# 6   Gopal         IT  110000.0
# 7   Rohit         HR  120000.0
# 8  Rakesh    Finance  130000.0
# 9  Sanjay         IT  140000.0>


#20 data
Employee = {
    "Staff ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    "Name": ["Ram", "Hari", "Sita", "Gita", "Ramesh", "Suresh", "Gopal", "Rohit", "Rakesh", "Sanjay", "Anil", "Bimal", "Chitra", "Dipak", "Esha", "Firoz", "Gita", "Hari", "Isha", "Jitendra"],
    "Address": ["Kathmandu", "Lalitpur", "Bhaktapur", "Pokhara", "Biratnagar", "Dharan", "Butwal", "Bharatpur", "Janakpur", "Birgunj", "Kathmandu", "Lalitpur", "Bhaktapur", "Pokhara", "Biratnagar", "Dharan", "Butwal", "Bharatpur", "Janakpur", "Birgunj"],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Contact": ["9800000001", "9800000002", "9800000003", "9800000004", "9800000005", "9800000006", "9800000007", "9800000008", "9800000009", "9800000010", "9800000011", "9800000012", "9800000013", "9800000014", "9800000015", "9800000016", "9800000017", "9800000018", "9800000019", "9800000020"],
    "Designation": ["Manager", "Assistant Manager", "Senior Executive", "Executive", "Manager", "Assistant Manager", "Senior Executive", "Executive", "Manager", "Assistant Manager", "Senior Executive", "Executive", "Manager", "Assistant Manager", "Senior Executive", "Executive", "Manager", "Assistant Manager", "Senior Executive", "Executive"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000, 210000, 220000, 230000, 240000],
    "Provident Fund": [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000],
    "Net Salary": [45000, 54000, 63000, 72000, 81000, 90000, 99000, 108000, 117000, 126000, 135000, 144000, 153000, 162000, 171000, 180000, 189000, 198000, 207000, 216000]   
}
df = pd.DataFrame(Employee)
print(df) 

# output:
#      Staff ID      Name     Address Department     Contact        Designation  Salary  Provident Fund  Net Salary
# 0        101       Ram   Kathmandu         IT  9800000001            Manager   50000            5000       45000
# 1        102      Hari    Lalitpur         HR  9800000002  Assistant Manager   60000            6000       54000
# 2        103      Sita   Bhaktapur    Finance  9800000003   Senior Executive   70000            7000       63000
# 3        104      Gita     Pokhara         IT  9800000004          Executive   80000            8000       72000
# 4        105    Ramesh  Biratnagar         HR  9800000005            Manager   90000            9000       81000
# 5        106    Suresh      Dharan    Finance  9800000006  Assistant Manager  100000           10000       90000
# 6        107     Gopal      Butwal         IT  9800000007   Senior Executive  110000           11000       99000
# 7        108     Rohit   Bharatpur         HR  9800000008          Executive  120000           12000      108000
# 8        109    Rakesh    Janakpur    Finance  9800000009            Manager  130000           13000      117000
# 9        110    Sanjay     Birgunj         IT  9800000010  Assistant Manager  140000           14000      126000
# 10       111      Anil   Kathmandu         IT  9800000011   Senior Executive  150000           15000      135000
# 11       112     Bimal    Lalitpur         HR  9800000012          Executive  160000           16000      144000
# 12       113    Chitra   Bhaktapur    Finance  9800000013            Manager  170000           17000      153000
# 13       114     Dipak     Pokhara         IT  9800000014  Assistant Manager  180000           18000      162000
# 14       115      Esha  Biratnagar         HR  9800000015   Senior Executive  190000           19000      171000
# 15       116     Firoz      Dharan    Finance  9800000016          Executive  200000           20000      180000
# 16       117      Gita      Butwal         IT  9800000017            Manager  210000           21000      189000
# 17       118      Hari   Bharatpur         HR  9800000018  Assistant Manager  220000           22000      198000
# 18       119      Isha    Janakpur    Finance  9800000019   Senior Executive  230000           23000      207000
# 19       120  Jitendra     Birgunj         IT  9800000020          Executive  240000           24000      216000
