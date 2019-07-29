import pandas as pd
import numpy as np

order = pd.read_table('meal_order_info.csv',sep=',',encoding='gbk',engine='python')
print('原始数据：\n',order.shape)

#由于表中的日期数据为字符中类型，所以在进行日期操作之前，需要所它们转换成TimeStape
order['use_start_time'] = pd.to_datetime(order['use_start_time'])
order['lock_time'] = pd.to_datetime(order['lock_time'])

#时间差
order['time']= order['lock_time'] - order['use_start_time']

#异常值的处理
#1.判断这一列是否有空值，如果有删除该行数据
index_null = order.index[order['time'].isnull()]

#删除
order.drop(labels=index_null,axis=0,inplace=True)
print('剔除空值后表的数据：\n',order.shape)

#2.关于错误值（负值）的清洗，lock_time<start_time
mask = order['lock_time']<order['use_start_time']
# print(mask)
index_fu = order.index[mask]
order.drop(labels=index_fu,axis=0,inplace=True)
print('剔除time为负值后表的数据：\n',order.shape)

# #3.关于异常值的清洗，点餐时间大于1天为异常数据
# print(order['time'].max())
print(order['time'].head(100))
# fp = pd.ExcelWriter('qingxi.xlsx')
# order.to_excel(fp)
# fp.save()

#str

# 序列.str,表示将序列中的元素（按行），以字符串的形式展示
# order['time'].astype('str')#0 days 00:12:00.000000000
# order['time'].astype('str').str #‘0 days 00:12:00.000000000’

# order['time'].astype('str').str[0]#字符串第一位的值


#生成过滤序列【False,True.....】,把True过滤掉
mask = (order['time'].astype('str').str[0]).astype('int')>0
index_exception = order.index[mask]
order.drop(labels=index_exception,axis=0,inplace=True)

print('异常值清洗后的表的数据为：',order.shape)

print(order['time'].min())
print(order['time'].max())
print(order['time'].mean())







