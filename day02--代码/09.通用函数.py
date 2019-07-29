import numpy as np

x = np.array([1,3,5])
y = np.array([2,3,6])
result = x==y
print(result)#[False  True False]
print(np.all(result))#False
print(np.any(result))#True

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
x = np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3]])
# y = np.array([1,2,3])
# z = x+y
# print(z)
y = np.array([1,2,3,4]).reshape((4,1))
z = x+y
print(z)



