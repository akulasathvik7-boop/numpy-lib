import numpy as np 

""" 
it will retireve the data 

upon the conditions >,< , !=

return TRUE or FALSE

boolean masking is 10times faster than the loops

"""

lis=[10,20,30,40,50]

arr=np.array([lis])

print(arr[arr>=20])
