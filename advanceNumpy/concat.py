import numpy as np

"""

np.concatenate((arr1, arr2), axis)
arr1, arr2 => arrays to concatenate
axis => axis along which to concatenate

"""
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.concatenate((arr1, arr2), axis=0)
print(result)