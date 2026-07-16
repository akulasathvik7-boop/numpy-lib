import numpy as np 
"""

stacking(arrays, axis)
arrays => list of arrays to stack
axis => axis along which to stack

"""

arr1=np.array([[1,2,3,4]])
arr2=np.array([[5,6,7,8]])

# result=np.stack((arr1, arr2), axis=0)
# print(result)

print(np.vstack((arr1, arr2))) # vertical stack
print(np.hstack((arr1, arr2))) # horizontal stack