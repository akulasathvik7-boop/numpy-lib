import numpy as np  
"""
converting mutli dim into 1d

.ravel()=>view

.flatten()=>copy
"""

lis=[[1,2,3],[4,5,6]]

arr=np.array(lis)
print(arr.ravel())
print(arr.flatten())