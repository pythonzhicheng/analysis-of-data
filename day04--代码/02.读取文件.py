
import pandas as pd

order = pd.read_table('meal_order_info.csv',sep=',',encoding='gbk')
print(order)

print('在转换之前lock_time的类型:',type(order['lock_time']))#<class 'pandas.core.series.Series'>
print('在转换之前lock_time的类型:',order['lock_time'].dtypes)#object
print('在转换之前lock_time的类型:',type(order['lock_time'][0]))#<class 'str'>

order['lock_time'] = pd.to_datetime(order['lock_time'])
print('在转换之后lock_time的类型:',type(order['lock_time'][0]))#<class 'pandas._libs.tslib.Timestamp'>

#对日期进行操作
#pandas支持日期范围
print('最小的时间为：',pd.Timestamp.min)#1677-09-21 00:12:43.145225
print('最大的时间为：',pd.Timestamp.max)#2262-04-11 23:47:16.854775807

#年、月、日、星期
year = [i.year for i in order['lock_time']]
month = [i.month for i in order['lock_time']]
day = [i.day for i in order['lock_time']]
hour = [i.hour for i in order['lock_time']]
weekday_name = [i.weekday_name for i in order['lock_time']]
print('lock_time中的星期名称数据前5个：',weekday_name[:5])
print(hour)

#操作
time_delta = order['lock_time']- pd.to_datetime('2017.1.1')
print('距离2017年1月1日0点0时0分后的数据：',time_delta[:5])
print(time_delta.dtypes)#timedelta64


a = order['lock_time'][0]
print(a.ctime())
print(a.time(),type(a.time()))
# https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.Timestamp.html
# l_t =[i.time() for i in order['lock_time']]
# print(type(l_t))
# print('min:',l_t.min())
# print('max:',l_t.max())









