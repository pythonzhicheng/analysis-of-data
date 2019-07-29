import numpy as np

arr = np.arange(20).reshape(4,5)
print('arr:\n',arr)

result_sum_0 = np.sum(arr,axis=0)#沿着纵轴计算
print(result_sum_0)
result_sum_1 = np.sum(arr,axis=1)#沿着横轴计算
print(result_sum_1)

result_mean_0 = np.mean(arr,axis=0)
print(result_mean_0)

#axis缺失的情况
print('axis缺失的情况,求整个数组的和：',np.sum(arr))
print('axis缺失的情况,求整个数组的均值：',np.mean(arr))

result_cumsum = np.cumsum(arr)
print('result_cumsum:',result_cumsum)

# arr = np.arange(1,7)
# result_comprod = np.cumprod(arr)
# print('result_comprod:',result_comprod)

print(np.min(arr,axis=0))
print(np.max(arr,axis=1))
print(np.std(arr,axis=1))
print(np.var(arr,axis=1))





