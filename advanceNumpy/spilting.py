import numpy as np
"""
split(arr, indices_or_sections, axis)
arr => input array
indices_or_sections => number of equal arrays to return or list of indices at which to split
axis => axis along which to split

"""

arr=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
# result=np.split(arr, 2, axis=1) # split into 2 equal  
print(np.split(arr, 12, axis=1)) # split at index 1 and 3