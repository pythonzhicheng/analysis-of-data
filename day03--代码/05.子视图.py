#创建子图：
# 子视图，本质上是多个基础图形绘制过程的叠加，即分别在同一个画布上不同子图上进行绘制。

import matplotlib.pyplot as plt
import numpy as np

rad = np.arange(0,np.pi*2,0.01)
#第一组数据
y1 = rad**2
y2 = rad**4

#绘制
#确定画布的大小，创建一个8*6的画布，并设置dpi=80
F = plt.figure(figsize=(8,6),dpi=80)
#创建并指定子视图
F.add_subplot(2,1,1)

#确定刻度范围
plt.xlim((0,1))
plt.ylim((0,1))

#数据
plt.plot(rad,y1)
plt.plot(rad,y2)

#图例
plt.legend(['y=x^2','y=x^4'])

#第二张图
s1 = np.sin(rad)
c2 = np.cos(rad)

F.add_subplot(2,1,2)

#常用
plt.xticks([0,np.pi/2,np.pi,np.pi*3/2,np.pi*2])

#数据
plt.plot(rad,s1)
plt.plot(rad,c2)
plt.legend(['sin','cos'])

plt.show()

