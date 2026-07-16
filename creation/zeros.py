import numpy as np

#creating the zeroes defaultly
#np.zeros()

#np.zeros(shape)

filled_zeros=np.zeros((3))
print(type(filled_zeros))


filled_zeros=np.zeros(4,dtype=int)#default dtype is float so we metinoned dtype=int to get integers
print(filled_zeros)

arr=np.zeros((2,3))
print(arr)

arr=np.zeros((2,3), dtype=str)
print(arr)


arr=np.zeros((2,3),dtype=bool)
print(arr)

arr=np.zeros((2,3),dtype=complex)
print(arr)

a = np.zeros((2,3))
a[0][1] = 5
print(a)


a = np.zeros((2,3))
print(a[1])