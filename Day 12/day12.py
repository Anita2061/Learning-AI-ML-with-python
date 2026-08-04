import numpy as np
stores=np.array([
    [120,135,150,145,160,170,180],
    [80,90,85,95,100,110,105],
    [60,55,70,65,75,80,85],
    [200,210,205,220,230,240,250],
    [150,145,160,170,180,190,200]
])
print (np.shape(stores))
# output:
#     (5, 7)

total_product= np.sum(stores, axis=0)
print(total_product)
# output:
#     [610 635 670 695 715 750 770]


total_product_by_day=np.sum(stores, axis=1)
print( total_product_by_day)
# output:
#     [990 640 520 1480 1120]

print(np.max(total_product))
# output:
#     770

print(np.max(total_product_by_day))
# output:
#     1480

print(np.average(total_product))
# output:
#     695.0

print(total_product[total_product>180])
# output:
#     [610 635 670 695 715 750 770]

new_product= total_product*1.10
print(new_product)
# output:
#     [671. 708.5 737. 764.5 786.5 825. 847.]

new_average= np.mean(stores, axis=1)
print(new_average>150)
# output:
#     [ True False False  True  True]

print(np.where(total_product<150))
# output:
#     (array([0, 1, 2]),)


bonus= np.where(stores>200, 20,0)
print(bonus)
# output:
#  [[ 0  0  0  0  0  0  0]
#  [ 0  0  0  0  0  0  0]
#  [ 0  0  0  0  0  0  0]
#  [ 0 20 20 20 20 20 20]
#  [ 0  0  0  0  0  0  0]]
