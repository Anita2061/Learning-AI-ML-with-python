#indexing or accessing arrays
#2D Array
import numpy as np
marks = np.array ([
    [80, 85, 60],
    [50, 60, 90],
    [88, 77, 66]
])
print(marks.ndim)
print(marks[1][2])  #(row, column)
print(marks[:,1]) 
  
# output:
# 2
# 90
#[85 60 77]   



#3D Array
marks=np.array([
    [[10, 20], [30, 40]],
    [[50, 60], [70, 80]]
])
print(marks.ndim)
print(marks[0][1]) 
print(marks[1][0]) 
print(marks[0][0][1])  #(layer, row, column)

# output:
# 3
# [30 40]
# [50 60]    
# 20 