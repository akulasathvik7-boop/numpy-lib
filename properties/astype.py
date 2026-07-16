import numpy as np

#to check the dimension of the array
#np.ndim()=>return the dimension of the array

lis2=[[1,2,3],[1,2,3]]
float_lis=[1.0,2.0,3.0,4.0,5.0]

arr1=np.array(lis2)
arr2=np.array(float_lis)
print(arr1.dtype)
print(arr2.dtype)

print(arr1.astype(float).dtype)
print(arr2.astype(int).dtype)