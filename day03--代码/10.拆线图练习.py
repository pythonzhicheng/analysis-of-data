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

plt.figure()

#参数简写：'颜色点的形状线的样式'
plt.plot(values[:,0],values[:,3],'bs-')
plt.plot(values[:,0],values[:,4],'ro--')
plt.plot(values[:,0],values[:,5],'g*-.')

plt.show()














