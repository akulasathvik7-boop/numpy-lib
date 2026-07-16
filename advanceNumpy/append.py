import numpy as np 

'''
np.append(arr, values, axis)
arr=>array to which we want to append the values
values=>values to append
axis=>axis along which we want to append the values
'''

lis=[1,2,3,4,5]
arr=np.array(lis)
arr1=np.append(arr, [6,7,8])
print(arr1)