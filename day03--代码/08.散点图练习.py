
#练习：
# 使用不同颜色、不同形状的点，绘制2000~2017年间各产业各季度国民生产总值 、的散点图
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

plt.scatter(values[:,0],values[:,3],c='red',marker='D')
plt.scatter(values[:,0],values[:,4],c='blue',marker='o')
plt.scatter(values[:,0],values[:,5],c='yellow',marker='v')

plt.show()


