import numpy as np

#1.排序
# (1)sort()函数---直接排序
# 用法：arr.sort()
# axis=0表示沿纵轴排序
# axis=1~~~~~~横轴~~~
arr = np.array([[4,3,2],[2,1,4]])
print(arr)
'4,3,2' \
'2,1,4'
# arr.sort()
# print(arr)
'[[2 3 4]'
'[1 2 4]]'
arr.sort(axis=0)
print(arr)

# 2间接排序---不改变原始数据
# （1）argsort()函数
# 返回值为重新排序后值的下标
arr = np.array([2,1,0,5,3])
arr1 = arr.argsort()
print('原始数据：\n',arr)
print('排序后的数据：\n',arr1)

for i in arr1:
    print(arr[i],end='~')

# （2）lexsort()函数
# 返回值是按照最后一个传入数据排序的。eg:np.lexsort((a,b,c))
a = np.array([3,2,6,4,5])
b = np.array([50,30,40,20,10])
c = np.array([400,300,600,100,200])
d = np.lexsort((a,b,c))#[3 4 1 0 2]
print(d)