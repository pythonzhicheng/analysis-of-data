import numpy as np
# 1.unique函数
# 通过unique函数可以找出数组中的唯一值并返回已经排序的结果。
arr = np.array([1,2,3,1,2,3])
result = np.unique(arr)
print(result)

#2.tile(A,reps)函数
#主要有两个参数，参数'A'指定重复的数组，
# 参数‘reps’指定重复的次数。
arr = np.arange(5)
arr_3 = np.tile(arr,3)
print(arr_3)

#3.repeat()函数
# def repeat(a, repeats, axis=None):
# axis=1表示按列进行元素重复
arr2 = np.random.randint(0,10,size=(3,3))
print('arr2:\n',arr2)
arr2_2_0 = np.repeat(arr2,2,axis=0)
print('按行重复：\n',arr2_2_0)
arr2_2_1 = np.repeat(arr2,2,axis=1)
print('按列重复：\n',arr2_2_1)

#repeat和tile两个函数的区别：
#两个函数都能够对数组进行“重复”，
#区别在于tile函数是地数组进行重复，repeat是对元素进行重复。
arr_tile_2 = np.tile(arr2,2)
print('tile是对整个数组进行重复：\n',arr_tile_2)

#拓展：
# 另外一写法
# arr2.repeat(2)

