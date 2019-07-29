#numpy
# Numpy的主要对象是同种元素的多维数组。
# 特点：这是一个所有元素都是一种类型、通过一个正整数元组索引的元素表格。
# 使用C写的

import numpy as np

arr1 = np.array([1,2,3])
#数组的秩
# 轴的个数称为秩
# 轴（axes）是数组的维度
print(arr1.ndim)#结论：一维数组秩为1，二维数组秩为2
print(arr1)

#数组的维度
print(arr1.shape)#(3,)---返回的类型，只有一个元素的元组。
#此处数组的维度为1，3表示轴的长度。

#二维数组
arr2 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print('arr2的秩为：',arr2.ndim)#2
print('arr2的维度：',len(arr2.shape))#2 ------(3, 4)
print(arr2)

# 二、常用属性
# 1.ndim
#2.shape

arr3 = np.array([1,2,3,4,5,6])
print(arr3.shape,arr3)
arr3.shape = (2,3)
print(arr3)


# (3)size
# 元素总和
print(arr3.size)#
if len(arr3.shape) == 2:
    print('元素总个数：',arr3.shape[0]*arr3.shape[1])
elif len(arr3.shape) == 1:
    print('元素总个数：',arr3.shape[0])

#dtype
#一个用来描述数组中元素类型的对象，可以通过创造或指定python类型。
print(arr3.dtype)#int32
#itemsize
# 数组中每个元素的字节大小。
print(arr3.itemsize)#4个字节
#data---数组的内存地址，是数据存储在内存的缓冲区。
print(arr3.data)#<memory at 0x0000000003568C18>
print(arr3[1])