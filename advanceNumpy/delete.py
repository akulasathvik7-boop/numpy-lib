import numpy as np 
"""
delete(arr, obj, axis)
arr => input array
obj => index of the element to delete
axis => axis along which to delete

"""

arr=np.array([1,2,3,4,5])
print(np.delete(arr,2, axis=0)) # delete 3rd element