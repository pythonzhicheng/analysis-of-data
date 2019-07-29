import pandas as pd

##1.检测处理重复值
"""
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K0', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': [1, 1, 2, 3],
                      'D': [2, 2, 4, 6],
                      'E': [1, 1, 2, 3]})
# （1）单列去重：==》去行
data_drop = right['key1'].drop_duplicates()
# keep:保留第几个重复值，默认为first,last,false:都不保留
print(len(data_drop))
# （2）对整个表去重==》去行
shape_det = right.drop_duplicates(subset=['key1', 'key2'])
print(shape_det)
"""

# （3）特征值重复==》去列(计算相似度)

# method={'pearson', 'kendall', 'spearman'} or callable
#             * pearson : standard correlation coefficient
#             * kendall : Kendall Tau correlation coefficient
#             * spearman : Spearman rank correlation
#             * callable: callable with input two 1d ndarray

'```````````````````````````````````````````````'
# corr_det = right[['C', 'D', 'E']].corr(method='kendall')
# print(corr_det)
detail = pd.read_excel(r'meal_order_detail.xlsx')
"""
corr_det = detail[['counts','amounts']].corr()
print(corr_det)
#求相似为1的布尔数组
mask = corr_det == 1
print(mask)
#遍历求与每个columns相似的列索引
index1 = corr_det.index
columns = corr_det.columns
print(index1)
print(index1[mask['counts']])
"""

##2.检测处理缺失值
'''
print(detail.shape)
isnull_sum = detail.isnull().sum()
mask = detail.shape[0] == isnull_sum
labels = isnull_sum.index[mask]
print(labels)
detail.drop(labels, axis=1, inplace=True)
print(detail.shape)


##dropna:删除缺失值的方法
detail.dropna(axis=0, how='all', inplace=True)
# any:或   all：全部
print(detail.shape)

##填充空值：
# detail =detail.fillna(0)
# 或者是
detail.fillna(0, inplace=True)
print(detail.isnull().sum())
##3.插值法：
import numpy as np
from scipy.interpolate import interp1d

x = np.array([1, 2, 3, 4, 5, 8, 9, 10])
y1 = np.array([2, 8, 18, 32, 50, 128, 162, 200])
y2 = np.array([3, 5, 7, 9, 11, 17, 19, 21])

Linear = interp1d(x, y2, kind='linear')  ##线型拟合插值
print(Linear([6, 7]))
# 非线性插值
from scipy.interpolate import lagrange

# 非线性可以拟合线型  只不过是效率慢
Larg = lagrange(x, y2)
print(Larg([6, 7]))

# 样本插值属于非线性插值
from scipy.interpolate import spline

print(spline(x, y1, xnew=np.array([6, 7])))
'''

##============标准化方式
"""
# （1）离差标准化  x1 = (x-min)/(max-min)
data = (detail['amounts'] - (detail['amounts'].min())) / (detail['amounts'].max() - (detail['amounts'].min()))
print(data)

# (2)标准差标准化：使得数据的均值为0，标准差为1
# x1 = x-u/σ   u：均值  σ:标准差
data = (detail['amounts'] - detail['amounts'].mean()) / detail['amounts'].std()
print(data)

# 小数定标标准化
# x1=x/10^k    
import numpy as np

x1 = detail['amounts'] / 10 ** (np.ceil(np.log10(detail['amounts'].abs().max())))
print(x1)
"""

##============================哑变量处理

# 将类别型数据转换为one-hot编码===》数值型矩阵
# print(pd.get_dummies(detail['dishes_name'].head()))

# +=================离散化连续型数据
# 1.等宽法：可能使得不同的类别频率差值较大
price = pd.cut(detail['amounts'], 5)
print(price.value_counts())  ##统计每一列中不同类别有多少个
# value_counts:只适用于单列
# 2.等频法：
price = pd.qcut(detail['amounts'], 5)
print(price.value_counts())
