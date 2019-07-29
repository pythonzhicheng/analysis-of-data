import numpy as np
#1.生成随机数
# (1)random(n)函数
# 格式：np.random.random(n)
# 说明:生成一个数组，元素值域：[0,1),其中n表示个数
r1 = np.random.random(10)
print(r1)

#（2）rand（）
# np.random.rand(m,n,....)
# 说明：生成一个M x N x ...维的数组，元素值域：[0,1)
r2 = np.random.rand(3,4,5)
print(r2)

#(3)randn()
# 说明：生成数组，数组元素为正态随机数
r3 = np.random.randn(10000)#生成1000个随机数
print(r3)
#遵循大数定理
# import matplotlib.pyplot as plt
# plt.hist(r3)
# plt.show()

#（4）randint()
# 格式：random.randint(a,b)
# 值域：[a,b]
r4 = np.random.randint(2,10,size=(2,3))
print(r4)
np.random.shuffle(r4)
print(r4)

#（5）二项式---伯努力概型--只有两种可能。
a5 = np.random.binomial(5,0.5,size=(3,5))
print('a5',a5)









