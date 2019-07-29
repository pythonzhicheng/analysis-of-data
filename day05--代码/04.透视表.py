import pandas as pd
import numpy as np

detail = pd.read_excel('meal_order_detail.xlsx')

#透视表
#index=具体的列名 或者 index=[列名1,列名2]
detail_pivot = pd.pivot_table(detail[['order_id','counts','amounts']],index='order_id')
print('以order_id分组后创建透视表(均值):\n',detail_pivot.head())

#可以指定聚合函数
data = detail[['order_id','counts','amounts']]
detail_pivot = pd.pivot_table(data=data,index='order_id',aggfunc=np.sum)
print('以order_id分组后创建透视表(求和):\n',detail_pivot.head())

#我就想给你演示一下index参数后面可以跟一个列表,表示按照多个列名进行分组,行了吧
data = detail[['order_id','counts','amounts','dishes_name']]
result = pd.pivot_table(data=data,index=['order_id','dishes_name'],aggfunc=np.sum)
print('以order_id和dishes_name作为行分组键创建的透视表',result.head())

#演示的是列分组
result = pd.pivot_table(data=data,index='order_id',columns='dishes_name',aggfunc=np.sum)
print('以order_id为行分组键，以dishes_name为列分组键创建的透视表为：\n')
print(result.head())


#演示values参数---默认对全部数据进行聚合
# result =pd.pivot_table(data=data,index='order_id',values='counts',aggfunc=np.sum)
result =pd.pivot_table(data=data,index='order_id',aggfunc=np.sum)
print(result.head())

#演示当有缺失值时，填充值的设置
result = pd.pivot_table(data=data,index='order_id',columns='dishes_name',aggfunc=np.sum,fill_value=0)
print('将缺失值填充为数值0',result.head())

#演示margins参数
result = pd.pivot_table(data=data,index='order_id',columns='dishes_name',aggfunc=np.sum,fill_value=0,margins=True)
print('查看汇总数据：\n',result.head())






