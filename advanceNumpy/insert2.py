import numpy as np
"""
2d array insertion
np.insert(arr, index, value, axis)
arr->array in which we want to insert the value
index->index at which we want to insert the value
value->value which we want to insert
axis->axis along which we want to insert the value
"""
lis=[[1,2,3],[4,5,6]]   
arr=np.array(lis)
print(np.insert(arr, 1, 10, axis=0))#inserts 10 at index 1 in the flattened array
#axis=0 means we are inserting along the rows, so 10 will be inserted as a new row at index 1
#axis=1 means we are inserting along the columns, so 10 will be inserted as a new column at index 1
#axis=None means we are inserting in the flattened array, so 10 will be inserted at index 1 in the flattened array