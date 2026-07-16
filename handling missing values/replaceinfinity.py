import numpy as np

arr=np.array([1,2,np.inf])
print(np.isinf(arr))

cleaned_arr=np.nan_to_num(arr,posinf=10)
print(cleaned_arr)