import numpy as np

# 一、创建矩阵
# 1.mat函数
#方法一：
A = np.mat([[1,0,1,0],[-1,2,0,1],[1,0,4,1],[-1,-1,2,0]])
print(A)
#方法二：
B = np.mat('1 0 0 0;0 1 0 0; -1 2 1 0;1 1 0 1')
print(B)

# 1.matrix函数
# np.matrix

# 3.bmat函数：通过分块矩阵创建大矩阵。
A =  np.mat([[1,1],[1,1]])
B =  np.mat([[2,2],[2,2]])
C =  np.mat([[3,3],[3,3]])
D =  np.mat([[4,4],[4,4]])
big_mat = np.bmat([[A,B],[C,D]])
print(big_mat)


#矩阵运算
A = np.mat([[1,1],[1,1]])
B = np.mat([[2,2],[2,2]])
print(A*3)
print(A+B)

# A = np.mat([[1,2,3,4],[2,0,1,5]])
# B = np.mat([[1,0,2],[-1,1,3],[4,1,0],[2,3,4]])
# C = A*B
# print(C)

result = np.multiply(A,B)#对应元素相乘
print(result)

#矩阵属性
# T--->matr1.T
A = np.mat([[1,2],[1,3]])
print(A.T)
#H--->共轭转置
# A--->返回是自身数据的2维数组的一个视图




