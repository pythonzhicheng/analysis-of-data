
#rc参数往往用来设置线宽、线样式、点的类型、颜色

import matplotlib.pyplot as plt
import numpy as np



x = np.arange(0,1.1,0.01)
print(x)
y1 = x**2
y2 = x**4

#显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#设置正常显示符号，解决保存图像是符号‘-’显示方块
plt.rcParams['axes.unicode_minus'] = False

#可视化
plt.figure()

#常用设置
#1.标题
plt.title('函数关系图@sin/cos')

#x和y轴名称
plt.xlabel('x-sin')
plt.ylabel('y-cos')

#x和y轴刻度范围
plt.xlim((0,1))
plt.ylim((0,1))

#刻度间距
plt.xticks([0,0.5,1])
plt.yticks([0,0.4,0.8,1])

plt.plot(x,y1,color='red',linewidth=1,linestyle='-')
plt.plot(x,y2,linestyle='--')
plt.plot(x,x**3,linestyle='-.')
plt.plot(x,x**5,linestyle=':')

#图例
plt.legend(['y=x^2','y=x^4'])

#保存
plt.savefig('img/案例2.png')
plt.show()
