import pandas as pd

detail = pd.read_excel('output.xlsx')

#DataFrame常用属性
print(detail.shape)  #形状
print(detail.size)  #元素总个数
print(detail.ndim)   #维数
print(type(detail))  #DataFrame类型

#取值--返回是一个数组
# print(detail.values)  #表里除表头以外所有的值
#
# print(detail['dishes_name'].values)  #该列的值
# print(type(detail['dishes_name'].values)) #<class 'numpy.ndarray'>

#获取列名，返回是一个数组
print(detail.columns)

#类型
print(detail.dtypes)

#索引
print(detail.index)

# 获取首尾数据
# n默认为5
print(detail.head(n=10))
print(detail.tail())