

#散点：主要用于分析特征间的相关关系。
#折线图：主要分析是自变量与因变量特征间趋势关系。

import matplotlib.pyplot as plt
import numpy as np
#通用设置
#输出设置
np.set_printoptions(threshold=np.NaN)

#显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#设置正常显示符号，解决保存图像是符号‘-’显示方块
plt.rcParams['axes.unicode_minus'] = False

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~编程代码区域~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

#1.数据加载
data = np.load('国民经济核算季度数据.npz')
columns = data['columns']
print(columns)
values = data['values']
print(values)


#2.可视化
plt.figure(figsize=(8,8))

#设置
plt.xlabel('年份')
plt.ylabel('生产总值（亿元）')
plt.title('2000~2017年季度生产总值散点图')

plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=30)


#散点图
plt.scatter(values[:,0],values[:,2],marker='o')

plt.show()







