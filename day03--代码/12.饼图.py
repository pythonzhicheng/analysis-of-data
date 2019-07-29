# 用折线图来绘制各个季度各产业的数据
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

#数据
x = values[-1,3:6]

#可视化
plt.figure()

#常用设置
plt.title('2017年第一季度各产业国民生产总值饼图')

#饼图
labels = ['第一产业','第二产业','第三产业']
plt.pie(x,explode=[0.1,0.01,0.01],labels=labels,
        autopct='%.1f%%')
plt.savefig('img/饼图.png')
plt.show()