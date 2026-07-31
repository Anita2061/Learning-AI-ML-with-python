#correlation
import numpy as np

hours = np.array([1, 2, 3, 4, 5])

marks = np.array([30, 40, 50, 60, 70])

marks2 =np.array([70, 60, 50, 40, 30])

print(np.corrcoef(hours, marks))
# output:   (positive correlation)
# [[1. 1.]
#  [1. 1.]]

print(np.corrcoef(hours, marks2))
# output:    (negative correlation)
# [[ 1. -1.]
#  [-1.  1.]]



#coveriance
temp = np.array([20, 30, 35])

icecream = np.array([200, 250, 300])

print(np.cov(temp, icecream))
# output:
# [[  58.33333333  375.        ]
#  [ 375.         2500.        ]]