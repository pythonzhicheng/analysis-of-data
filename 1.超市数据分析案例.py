import pandas as pd
import matplotlib.pyplot as plt
#
order = pd.read_csv(r'order-14.3.csv', encoding='gbk', engine='python')
# print(order.columns)
#
# ##处理数据：
# mask = order['销量'] < 0
# index1 = order.index[mask]
# order.drop(index1, axis=0, inplace=True)
#
# #1.1、哪些类别的商品比较畅销？
# # print(order[['类别ID', '销量']].groupby(by='类别ID').sum().reset_index())
#       # .sort_values(by='销量', ascending=False).index.head())
#
# #补充：
# # (1).reset_index(): 对分组聚合后的dataframe, 重设索引值，将默认的行索引变为正常的一列属性；
# #(2). sort_values(by='排序列索引'，ascending = ‘排序方式：False==>降序排序， True==>升序排序’ )
#
# #2、哪些商品比较畅销？
#(1).透视表：根据商品ID进行分组：
table = pd.pivot_table(order[['商品ID', '销量']], index='商品ID', values='销量', aggfunc='sum')

#(2).重设索引，排序
sort_table = table.reset_index().sort_values(by='销量', ascending=False)

#(3)获取排序的前几个值：
print(sort_table['商品ID'].head())

#
# #3.3、求不同门店的销售额占比
# # order['amounts'] = order['单价']*order['销量']
# # grouby_sum = order[['门店编号', 'amounts']].groupby(by='门店编号').sum()
# #
# # #可视化：
# # plt.figure(figsize=(8, 8))
# # #不同门店编号对应的销售额：
# # x = grouby_sum['amounts'].values
# # #每个分块距离圆心距离：
# # explode = [0.01, 0.1, 0.01]
# # #每一个x对应的labels，''
# # labels = grouby_sum.index
# # plt.pie(x, explode=explode, autopct='%1.1f%%', labels=labels)
# # plt.show()
import numpy as np
data = np.array([[3], [4]])##values
print(pd.DataFrame(data=data))
# #
# # data=['1','2']
# # print(pd.Series(data=data))
# # data['columns'][:]
# # # data.loc[0:2,列]
# # # data.loc[data['age']>18, ['name', 'age']]
# #
# # bool_arr = data['age']>18
# # data[bool_arr]
#
# x = np.random.randn(10000)
# plt.hist(x, 20)
# plt.show()
#
# # pd.read_excel()
#


##############=================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1.表堆叠~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##concat ==>堆叠：根据行、列索引进行表的拼接，而不看元素取值；

# detail1 = pd.read_excel(r'C:\Users\ibm\Desktop\数据分析阶段所有数据\meal_order_detail.xlsx',sheetname=0)
# detail2 = pd.read_excel(r'C:\Users\ibm\Desktop\数据分析阶段所有数据\meal_order_detail.xlsx',sheetname=1)
# print(detail1.shape)
# print(detail2.shape)
# print(pd.concat((detail1, detail2), axis=0, join='inner').shape)

# data = np.array([[1, 2],[2, 3], [4, 5]])
# df1 = pd.DataFrame(data, columns=['A', 'a'])
# df2 = pd.DataFrame(data, columns=['A', 'B'])
# print(df1)
# print(df2)
# print(pd.concat([df1, df2],axis=0, join='outer'))
# print(pd.concat([df1, df2],axis=0, join='inner'))
# print(pd.concat([df1, df2], axis=1, join='inner'))
# print(pd.concat([df1, df2], axis=1, join='outer'))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2.主键合并~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##merge: 主键合并：根据两个表中元素取值是否相同来进行表拼接；（跟行列索引无关）
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                          'A': ['A0', 'A1', 'A2', 'A3'],
#                         'B': ['B0', 'B1', 'B2', 'B3']})
# # print(left)
#
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                          'C': ['C0', 'C1', 'C2', 'C3'],
#                          'D': ['D0', 'D1', 'D2', 'D3']})
# print(right)

##1.一个主键：（两表中主键名称一样）
# print(pd.merge(left, right, how='right', on='key1'))

#2.多个主键：（两表中主键名称一样）
# print(pd.merge(left, right, how='left', on=['key1', 'key2']))

#3.当两个表中，主键名称不一样时，主键合并：
# print(pd.merge(left, right, how='inner', left_on='key2', right_on='key1'))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2.重叠合并~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#当两个表结构基本相同，但是两个表中都有缺失数据，可以利用重叠合并来拼接数据，构建一个完整的表：
# df1.combine_first(df2)：利用df2来完善df1, 当df1与df2中都有数据的时候，以df1为准；（df1为主表）

# dict1 = {'ID':[1,2,3,4,5,6,7,8,9], 'System':['w10','w10',np.nan,'w10',np.nan,np.nan,'w7','w7','w8']}
# dict2 = {'ID':[1,2,3,4,5,6,7,8,9], 'System':[np.nan,np.nan,'w7','w7','w7','w7','w8',np.nan,np.nan]}
# df1 = pd.DataFrame(dict1)
# df2 = pd.DataFrame(dict2)
# print(df1)
# print(df2)
# print(df1.combine_first(df2))
# print(df2.combine_first(df1))
