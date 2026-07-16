import numpy as np 

#filling with the same values in the array wih full function

#np.full(d,n)

#np.full(dim,num)

full_array=np.full(3,5)
print(full_array)


full_array=np.full((2,3),5)
print(full_array)

a = np.full((2,2), "Hello")
print(a)

a = np.full((2,2), None)
print(a)

a = np.full((2,2),True)

print(a)