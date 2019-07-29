import numpy as np
#1.shape
#2.reshape
a1 = np.arange(15).reshape(-1,5)
print(a1)
#注意：reshape(m,n),如果说有一个参数为-1时，
# 那么reshape函数会根据另一个参数的维度计算出数组的另外一个shape属性值

a2 = a1.reshape(-1)#将多维数组变换成一维数组
print(a2)

a3 = a1.reshape(-1,1)
print(a3)#生成的一定是个二维数组，行数会通过列数计算得来

a4 = a1.reshape(3,-1)
print(a4)

big_array = np.arange(10000).reshape(100,100)
print(big_array)
#注意：如果一个数组太大，在输出时Numpy自动省略中间部分而只打印两边元素。
#禁用Numpy的这种行为并强制打印整个数组，可以在打印之前设置如下：
# np.set_printoptions(threshold=np.NaN)
# print(big_array)

# 三、展平数组
# 1.ravel函数
# 说明：是reshape()函数的逆操作。不是在原数组上修改，而创建一个新数组
a1 = np.arange(10)
a2 = a1.reshape(2,5)
print(a1)
print('a2:',a2)
# [0,1,2,3,4]
# [5,6,7,8,9]
a3 = a2.ravel()
print(a3)#[0 1 2 3 4 5 6 7 8 9]

#2.flatten函数
# 说明：默认为横向展平，纵向展平需要加‘F’参数
a4 =a2.flatten()
print('a4:',a4)
a5 = a2.flatten('F')
print(a5)

#ravel和flatten区别
#都能够实现将多维数组降为一维数组，
# 区别在于返回的是拷贝（copy）还是返回的是视图（view）
# numpy.flatten()返回的是拷贝,对于拷贝所做的修改不会影响到原始数据。
#numpy.ravel()返回的是视图，会影响到原始数据
a1 = np.arange(10)
a2 = a1.reshape(2,5)
print('a2:',a2)

a5 = a2.flatten('F')
a5[0] = 100
print('a5:',a5)
print('a2:',a2)


# a3 = np.ravel(a2)
# a3[0] = 100
# print('a3:',a3)
# print('a2:',a2)





# a1 = [33,2,-1,22]
# print('a1_pre:',a1)
# # a1.sort()
# # print('a1_last:',a1)
#
# a2 = sorted(a1)
# print(a1)
# print(a2)





