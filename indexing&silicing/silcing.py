import numpy as np
import copy 
lis1=[1,2,3,4,5]


arr1=np.array(lis1)


print(arr1[0:3])#returns the values from index 0 to 2

print(arr1[::2])#returns the values from index 0 to 4 with a step of 2

print(arr1[::-1])#returns the values from index 4 to 0
print(arr1[::-2])#returns the values from index 4 to 0 with a step of 2

arr2=arr1.copy()#creates a copy of the array
print(arr2[0:3])#returns the values from index 0 to 2

arr3=copy.deepcopy(arr1)#creates a deep copy of the array
print(arr3[0:3])#returns the values from index 0 to 2