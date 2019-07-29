# Matlab--
import matplotlib.pyplot as plt
import numpy as np

#创建画布
# F = plt.figure()#创建一个空白画布，可以指定画布的大小、像素
# F.add_subplot()#创建并选中子视图，可以指定子视图的行数、列数和选中图片的编号
# 案例：绘制直接y = 2*x+1
# x = np.linspace(-1,1,50)
# y = 2*x+1
# print(x,y)

#创建画布
# plt.figure()
#
# # plot(x,y)绘制曲线
# plt.plot(x,y)
#
# #保存成图片
# plt.savefig('img/案例1.png')
# #显示画布
# plt.show()

#案例2：在同一画布中绘制两条曲线
#y1 = x^2
#y2 = x^4
x = np.arange(0,1.1,0.01)
print(x)
y1 = x**2
y2 = x**4

#可视化
plt.figure()

#常用设置
#1.标题
plt.title('line')

#x和y轴名称
plt.xlabel('x')
plt.ylabel('y')

#x和y轴刻度范围
plt.xlim((0,1))
plt.ylim((0,1))



#刻度间距
plt.xticks([0,0.5,1])
plt.yticks([0,0.4,0.8,1])

plt.plot(x,y1)
plt.plot(x,y2)

#图例
plt.legend(['y=x^2','y=x^4'])

#保存
plt.savefig('img/案例2.png')
plt.show()




