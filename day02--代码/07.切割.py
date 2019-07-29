import numpy as np

#切割数组
# 1.hsplit()和vsplit()
arr1 = np.array([[1,1,3,3],[2,2,4,4]])
print('arr1:\n',arr1)
arr6_subarray = np.hsplit(arr1,2)
print(arr6_subarray,type(arr6_subarray))
a1 = arr6_subarray[0]
print(type(a1))

arr7_subarray = np.vsplit(arr1,2)
print(arr7_subarray)



