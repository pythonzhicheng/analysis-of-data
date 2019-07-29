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


#把整个圆切成5份
dataLenth = 5

#角度范围---
angles = np.linspace(0,2*np.pi,dataLenth,endpoint=False)

#文字标签
labels = ['生存','输出','团战','KDA','发育']

#数值
data = [2,3.5,4,4.5,5]

#闭合
new_data = np.concatenate((data,[data[0]]))
new_angles = np.concatenate((angles,[angles[0]]))

#可视化
plt.figure()

#雷达图
plt.polar(new_angles,new_data,color='r',marker='o')

#刻度标签
plt.xticks(new_angles,labels)

#标题
plt.title('王者荣耀成绩')

plt.show()




