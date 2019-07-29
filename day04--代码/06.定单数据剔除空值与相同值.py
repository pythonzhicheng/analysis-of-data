import pandas as pd

detail = pd.read_excel('output.xlsx')
print(detail.describe())

col = detail.shape[1]
print('原始数据中列的个数：',col)

#获取所有列属性对应的describe,返回值为布尔值
colisNull = detail.describe().loc['count'] == 0
print(colisNull)
print(type(colisNull))

# 去除全为空值的列标准差为0的列
#注：标准差为0表示所有数据都是0，不适合做横向比较，不能用于分析

#1.剔除空值
for i in range(len(colisNull)):
    # print(colisNull[i])
    if colisNull[i]:
        detail.drop(colisNull.index[i],axis = 1,inplace= True)
        # print(colisNull.index[i])


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#2.剔除0值
stdisZero = detail.describe().loc['std'] == 0
print(stdisZero,type(stdisZero))#<class 'pandas.core.series.Series'>

for i in range(len(stdisZero)):
    if stdisZero[i]:
        detail.drop(stdisZero.index[i],axis=1,inplace=True)

col = detail.shape[1]
print('剔除空值后列的个数：',col)#剔除空值后列的个数： 9




