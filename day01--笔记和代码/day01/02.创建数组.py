import numpy as np
#方法有：
# 1.array()
# def array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
# eg：
a1 = np.array([1,2,3,4])
a2 = np.array([(1,2),(3,4)])
print(a2)
a3 = np.array([[1,2],[3,4]])
print(a3.dtype)

#dtype
a4 = np.array([[1,2],[3,4]],dtype=np.float32)
print(a4.dtype)


#2.arange()函数创建一维数组
# 格式：arange(起，止，步长)
# 注意：[start, stop)
a5 = np.arange(0,1,0.1)
print(a5)#[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9]

a6 = np.arange(0,90,1.5)
print(a6)#[ 0.   1.5  3.   4.5  6.   7.5]
# 通常无法准确预估元素个数，所以我们一般使用linspace
#3.使用linspace()函数
# 格式：def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None):
# 注意：[`start`, `stop`].
a7 = np.linspace(1,10,11)
print(a7)


# 4.logspace()---等比数例
# eg1：生成10^1~10^3之间的3个等比数值
a8 = np.logspace(1,3,3)
print(a8)#[   10.   100.  1000.]
#eg2:生成2^0~2^10,10
# 0 2 4 8 16 32 64....1024
a9 = np.logspace(0,10,11,base=2,dtype=np.int32)
print(a9)#[   1    2    4    8   16   32   64  128  256  512 1024]

#5.zeros/ones
# np.array([[0,0,0],[0,0,0]])
a10 = np.zeros((2,3))
print(a10)

a11 = np.ones((2,3))
print(a11)

#6.empty()
#该函数创建一个内容随机并且依赖于内存状态的数组。
a12 = np.empty((2,3))
print('a12:',a12)

# 7.eye()
# 生成N阶矩阵，对角线元素为1
a13 = np.eye(3)
print(a13)

#8.diag()函数
a14 = np.diag([1,2,3,4])
print(a14)



