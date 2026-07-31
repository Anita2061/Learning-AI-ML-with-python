#example
# : denote column
# :1 - column 1 agadi savai print garni
# 1: - column 1 paxi savai print garni

import numpy as np
marks=np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(marks[:2]) #column sabai print garni

# [[10 20 30]
#  [40 50 60]]

print(marks[1:]) #column 1 print garni

# [[40 50 60]]

print(marks[:, :2]) #column 2 ko agadi savai print garni

# [[10 20]
#  [40 50]]

print(marks[:,1:]) # column 1 ko paxi savai print garni

# [[20 30]
#  [50 60]]



#example
import numpy as np
marks=np.array([
[80, 85, 82],
[75, 88, 92],
[60, 70, 95]
])

print(marks[:2])

# [[80 85 82]
#  [75 88 92]]

print(marks[1:])

# [[75 88 92]
#  [60 70 95]]

print(marks[:, :2])

# [[80 85]
#  [75 88]
#  [60 70]]

print(marks[:,1:])

# [[85 82]
#  [88 92]
#  [70 95]]