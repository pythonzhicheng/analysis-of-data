import numpy as np

#数组元素的访问是通过“索引”来完成的。
a1 = np.arange(10)
print('a1:',a1)
print(a1[0])#0
print(a1[2:4])#[2,3]
print(a1[-1])#9

#修改
a1[0] = 100
a1[2:4]=200,300
print(a1[1::2])

#二维数组
a2 = np.arange(1,13,1).reshape(3,4)
print('a2:',a2)
print(a2[0][-1])#直接多下标来访问
print(a2[1,1])#
print(a2[1:,2:])#
print(a2[:,:])#全部行、列数据
print(a2[:,2])
print(a2[1:,0::2])




#python
# list001 = [[1,2,3,4],[5,6,7,8]]
# list001[0][-1]