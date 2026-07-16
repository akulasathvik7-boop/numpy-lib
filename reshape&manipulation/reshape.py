import numpy as np 

"""
rehape is used to 

change the dimensions of the array

without modifying the data (erripuka)
reshape(rows,columns)

"""

lis=[1,2,3,4,5,6]
arr=np.array(lis)
print(arr)
print(np.shape(arr))
print(np.ndim(arr))

arr1=arr.reshape(2,3)
print(arr1)
print(arr1.shape)
print(np.ndim(arr1))