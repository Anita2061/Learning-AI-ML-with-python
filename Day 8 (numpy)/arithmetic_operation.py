#ADD
import numpy as np
arr= np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr+10)

# output:
# [[20 30 40]
#  [50 60 70]]



#SUB
arr= np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr-10)

# output:
# [[ 0 10 20]
#  [30 40 50]]    



# np.mean()
arr= np.mean([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr)

# 35.0



# np.std()
arr= np.std([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr)

# 17.07825127659933



# np.max()
arr= np.max([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr)

# 60