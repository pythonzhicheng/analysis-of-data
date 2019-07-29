import numpy as np
# 1.组合数组
# (1)hstack()和vstack()函数
arr1 = np.arange(1,6,2)#[ 1  3  5]
arr2 = np.arange(7,12,2)#[7  9 11]
arr3 = np.hstack((arr1,arr2))
print('arr3:',arr3)
arr4 = np.vstack((arr1,arr2))
print('arr4:',arr4)
#注意：
# （1）如果两个数组元素个数不相等，横向组合不受影响，但纵向组合会报错。
# （2）在stack函数中，使用圆括号和方括号都可以。
#  (3)两个数组使用加号连接，其实是对应元素相加。
arr5 = arr1 + arr2
print('arr5:',arr5)

# （2）concatenate()和轴
# 默认为：axis=0，纵向；axis=1横向
print('~~~~~~~~~~~~~~~~~~~~~~~华丽的分隔线~~~~~~~~~~~~~~~~~~~~~~~~~~~')
arr1 = np.array([[1,1],[2,2]])
arr2 = np.array([[3,3],[4,4]])
#横向
#方法一：
arr3 = np.hstack((arr1,arr2))
print(arr3)
'''
[[1 1 3 3]
 [2 2 4 4]]'''
#方法二：
arr4 = np.concatenate((arr1,arr2),axis=1)
print('arr4:\n',arr4)

# temp1 = np.array([1,2,3,4])
# print(temp1.shape)#(4,)
#
# temp2 = np.array([[1,1],[2,2],[3,3]])
# print(temp2.shape)#(3,2)

#纵向
#方法一：
arr5 = np.vstack((arr1,arr2))
print(arr5)
#方法二：
arr6 = np.concatenate((arr1,arr2),axis=0)
print('arr6:\n',arr6)





