import numpy as np

# 练习：读取iris数据集中的花萼长度数据，
# 并且对其进行排序、去重、求和、累积和、均值、标准差、方差、最大值、最小值。

iris = np.loadtxt('iris_sepal_length.csv')
iris.sort()
print('花萼长度表为：\n',iris)

#去除重复值
print('去重后的花萼长度表为：\n',np.unique(iris))
print('花萼长度均值为：',np.mean(iris))
print('最大值：%f ----最小值：%f'%(np.max(iris),np.min(iris)))

#计算数据的标准差、方差
print('方差：%f ----标准差：%f'%(np.var(iris),np.std(iris)))






