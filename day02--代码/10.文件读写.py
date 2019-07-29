import numpy as np

#numpy文件读写主要有二进制的文件读写和文件列表形式的数据读写两种形式。
# 1.二进制读写
# （1）save()函数---写--->硬盘
x = np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3]])
np.save('x.npy',x)
# (2)load()函数---读
x_array = np.load('x.npy')
print(x_array)
#注意：存储的时候可以省略扩展名，但是读取时不可以。

#（3）savez()----可以将多个数组保存到一个文件当中
y = np.array([1,2,3,4,5,6])
np.savez('xy',x,y)

# 2.文本数据读取（txt,csv格式）
# (1)写
np.savetxt('x.txt',x,delimiter=',',fmt='%d')
# （2）读
x_array = np.loadtxt('x.txt',delimiter=',')
print(x_array)

# (3)genfromtxt()函数
# 面向结构化数组和缺失数据。
jobInfo = np.dtype([('name',np.str_,40),('number',np.int32),('loca',np.str_,16)])
jobs = np.loadtxt('jobs.txt',dtype=jobInfo,delimiter=',')
print(jobs)

jobs2 = np.genfromtxt('jobs.txt',dtype=jobInfo,delimiter=',')
print(jobs2)
