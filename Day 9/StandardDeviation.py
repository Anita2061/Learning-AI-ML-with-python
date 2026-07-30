# percentile
# np.percentile(varible, percentile value)

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 650])
print(np.percentile(arr,25))

# output:
# 32.5    (25th percentile)

print(np.percentile(arr,50))

# output:
# 55.0    (50th percentile)

print(np.percentile(arr,75))

# output:
# 77.5    (75th percentile)

print(np.percentile(arr,90))

# output:
# 91.0    (90th percentile)



# mean
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 650])
print(np.mean(arr))

# output:
# 109.0909090909091


# (outlier)
# upper fence - acceptable minimum range
# lower fence - acceptable maximun range



#variance
a = np.array([1 ,2 ,3, 4, 5, 6, 7, 8, 9, 10])
print(np.var(a))

# output:
# 8.25   (data are closer to each other)

b= np.array([1, 15, 30, 45, 60, 75, 90, 115, 130, 145])
print(np.var(b))

# output:
# 2178.2400000000002   (data are far from each other)