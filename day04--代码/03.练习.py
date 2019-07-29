import pandas as pd

order = pd.read_table('meal_order_info.csv',sep=',',encoding='gbk')
#将字符日期数据--->日期数据
order['lock_time'] = pd.to_datetime(order['lock_time'])
order['use_start_time'] = pd.to_datetime(order['use_start_time'])

check_time = order['lock_time'] - order['use_start_time']
print(type(check_time))#<class 'pandas.core.series.Series'>
print('用时最少的点餐时间为：',check_time.min())
print('用时最多的点餐时间为：',check_time.max())

#异常
for i in range(order.shape[0]):
    if order['lock_time'][i] < order['use_start_time'][i]:
        print(i)
        #剔除错误数据

#数据清洗还是处理完成之后
print('平均点餐时间为：',check_time.mean())

#营业时间
timemin = order['use_start_time'].min()
timemax = order['lock_time'].max()
print('订单最早的时间为：',timemin)
print('订单最晚的时间为：',timemax)

print('订单持续时间为：',timemax-timemin)





