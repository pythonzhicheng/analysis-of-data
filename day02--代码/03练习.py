# 自定义一个类型用来存储班级学员列表数据：
# （1）名称（32）
# （2）年龄
# （3）性别
# （4）成绩
import numpy as np
# df = np.dtype([('name',np.str_,32),('age',np.int16),('sex',np.str_,8),('score',np.float32)])
# std_arr = np.array([('lori',32,'男',99),('jam',22,'男',100),('tom',19,'女',99.5)],dtype=df)
# print(std_arr)

df = np.dtype([('name',np.str_,32),('age',np.int16),('sex',np.bool_),('score',np.float32)])
std_arr = np.array([('lori',32,1,99),('jam',22,1,100),('tom',19,0,99.5)],dtype=df)
print(std_arr)


#读取数据元素
pre2 = std_arr[:-1]
print(pre2)
print(pre2[0][0])
