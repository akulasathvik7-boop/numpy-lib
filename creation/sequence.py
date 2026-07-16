import numpy as np 


#sequencing of nums in array ysing arrange

#arrange()
#arange(start,stop,steps)


seq_array=np.arange(0,10,2)
print(seq_array)


arr=np.arange(4)
print(arr)

print(np.arange(10,1,-2))

print(np.arange(1,10,-1))

print(np.arange(5,6))

print(np.arange(0,1,0.2))

print(np.arange(5, dtype=float))


# print(np.arange(5, dtype=bool))

print(np.arange(5) > 0)

"""
0 → False
1,2,3,4 → True
"""