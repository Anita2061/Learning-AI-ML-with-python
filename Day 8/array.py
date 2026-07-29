import numpy as np

#1D Array
a= np.array([10, 20, 30, 40, 50, 60])
print(a)

#output:
# [10 20 30 40 50 60]



#2D Array
b= np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b)

# output:
# [[10 20 30]
#  [40 50 60]]   



#3D Array
c=np.array([
    [[10, 20], [30, 40]],
    [[50, 60], [70, 80]]
])
print(c)

# output:
# [[[10 20]
#   [30 40]]

# [[50 60]
#   [70 80]]]



#array.ndim (lato dimensional ho vanera patta lagaune)
import numpy as np
a= np.array([10, 20, 30, 40, 50, 60])
print(a.ndim)

b= np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b.ndim)

c=np.array([
    [[10, 20], [30, 40]],
    [[50, 60], [70, 80]]
])
print(c.ndim)

# output:
# 1
# 2
# 3



# array.size (array ko vitra kati ota data xa patta lagaune)
import numpy as np
a= np.array([10, 20, 30, 40, 50, 60])
print(a.size)

b= np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b.size)

c=np.array([
    [[10, 20], [30, 40]],
    [[50, 60], [70, 80]]
])
print(c.size)

# output:
# 6
# 6
# 8



# array.shape (kati ota row ta column xa vanne patta lagaune)
import numpy as np
a= np.array([10, 20, 30, 40, 50, 60])
print(a.shape)

b= np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b.shape)

c=np.array([
    [[10, 20], [30, 40]],
    [[50, 60], [70, 80]]
])
print(c.shape)

# output:
# (6,)
# (2, 3)
# (2, 2, 2)



# array.dtype(euta data store huda kati storage linxa vanne)
import numpy as np
a= np.array([10, 20, 30, 40, 50, 60])
print(a.dtype)

b= np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b.dtype)

c=np.array([
    [[10, 20], [30, 40]],
    [[50, 60], [70, 80]]
])
print(c.dtype)

# output:
# int64
# int64
# int64