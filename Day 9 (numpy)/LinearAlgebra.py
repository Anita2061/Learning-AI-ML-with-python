import numpy as np

# embedding = [0.25, 0.42, 0.45, 1.20, 0.57]
# vector = 1D array is called vector 
# vector Database
# RAG = vectorization = embedding to 1D array
# LLM = similarwise, nearby, semantic search


# matrix
a = np.array([1, 2, 3, 4]),
b = np.array([5, 6, 7, 8]) 
print(a+b) 

# output:
# [[ 6  8 10 12]]  

print(a*b) 

# output:
# [[ 5 12 21 32]]  

print(a@b) 
# output:
# [70]  


a = np.array([[1, 2], [3, 4]]),
b = np.array([[5, 6], [7, 8]])  
print(np.dot(a,b))
# output:
# [[[19 22]
 # [43 50]]]
 


a=np.array([[4, 7], [2, 6]])
print(np.linalg.inv(a))
# output:   (inverse)
# [[ 0.6 -0.7]
#  [-0.2  0.4]]

print(np.linalg.det(a))
# output:   (determinant)
# 10.000000000000002
  