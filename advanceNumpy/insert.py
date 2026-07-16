import numpy as np 

'''
np.insert(arr,index,value,axis)
arr=>array in which we want to insert the value

arr->array in which we want to insert the value
index->index at which we want to insert the value
value->value which we want to insert
axis->axis along which we want to insert the value

'''

lis=[1,2,3,4,5]
arr=np.array(lis)
print(np.insert(arr, 2, 10))