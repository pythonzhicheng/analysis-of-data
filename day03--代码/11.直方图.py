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


#刻度标签
label =['第一产业','第二产业','第三产业']
#eg：拿出2017年第一季度数据
value = values[-1,3:6]

#可视化
plt.figure()
plt.xticks(range(3),label)
plt.title('2017年第一季度各产业国民生产总值直方图')
plt.xlabel('产业')
plt.ylabel('生产总值（亿元）')

plt.bar(range(3),value,width=0.5)

plt.show()