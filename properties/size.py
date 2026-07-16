import numpy as np 

#to check the size of the array

#np.size()=>return the number of values presents in the array



lis=[[1,2,3],[1,2,3]]

np_size=np.size(lis)

print(np_size)

lis=[[[1,2],[1,2],[1,3]],[[1,2],[1,2],[1,3]],[[1,2],[1,3],[1,4]]]

np_size=np.size(lis)

print(np_size)

a = np.ones((2,5))

print(a.size)

a = np.array([])

print(a.size)