import numpy as np 

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.delete(arr,1, axis=0)) # delete 2nd row
print(np.delete(arr,1, axis=1)) # delete 2nd column
print(np.delete(arr, [0,2], axis=0)) # delete 1st and 3rd row
print(np.delete(arr, [0,2], axis=1)) # delete 1st and 3rd column