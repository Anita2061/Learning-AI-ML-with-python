#loop
#what is loop?


#single loop
for i in range(5):
     print(i)
     
#output:
# 0
# 1
# 2
# 3
# 4  



for i in range(6):
    print("*"*i) 
    
#output:
# *
# **
# ***
# ****
# *****      



for i in range(5):
    for j in range(2):
        print(i,j)
        
#output
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# 3 0
# 3 1
# 3 2
# 4 0
# 4 1
# 4 2



for i in range(5):
    for j in range(2):
        print("*","*")


for i in range(5):
    for j in range(5):
        print("*", end ="  ")
    print()
    
    
# output : 
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *     



for i in range(6):
    for j in range(i):
        print("*", end ="  ") 
    print()
    
# output:
# *  
# *  *  
# *  *  *  
# *  *  *  *  
# *  *  *  *  *     



for i in range(1,6):
    for j in range(1, i+1):
        print( j , end ="  ") 
    print()
    
#output:
# 1  
# 1  2  
# 1  2  3  
# 1  2  3  4  
# 1  2  3  4  5  



for i in range(5, 0, -1):
    for j in range(i):
        print("*", end ="  ") 
    print()
     
    
# output:
# *  *  *  *  *  
# *  *  *  *  
# *  *  *  
# *  *  
# * 



for i in range(5):
    for j in range(i):
        print(" ", end = " ")
    for j in range(5-i):
        print("*", end=" ")
    print()
    
# output:
#     * * * * * 
#       * * * * 
#         * * * 
#           * * 
#             *



for i in range(6):
     for j in range(6-i):
         print(" ", end = "")
         
     for j in range(i):
         print("*", end=" ")
     print()
     
#  output:    
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * *



n=5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for k in range(2 * i + 1):
        print("*", end = " ")
    print()
    
# output:
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * *    



n=5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for k in range(2 * i + 1):
        print("*", end = " ")
    print()
#lower 
for i in range(n - 2, -1 , -1 ):
    for j in range(n - 1 - 1):
        print(" ", end = " ")  
    for k in range (2*1+ 1):
        print("*", end =" ")
    print()
        
# output:
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
#       * * * 
#       * * * 
#       * * * 
#       * * *   
        
 
        
n=5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for k in range(2 * i + 1):
        print("*", end = " ")
    print()
#lower 
for i in range(n - 2, -1 , -1 ):
    for j in range(n - i - 1):
        print(" ", end = " ")  
    for k in range (2* i+ 1):
        print("*", end =" ")
    print()
         
# output:
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         *      
        
        
                       