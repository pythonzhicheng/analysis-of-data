import pandas as pd
import numpy as np

#读取数据
detail = pd.read_excel('output.xlsx',sheetname=0)

# lite_detail = detail[['order_id','counts','amounts','dishes_name']]
# detail_group =lite_detail.groupby(by='order_id')
#
# print(detail_group['order_id'])

#数据分析
# print('每个订单的均值：\n',detail_group.mean().head())
# print('每个订单的标准差：\n',detail_group.std().head())
# print('每个订单的大小为：\n',detail_group.size().head())

#任务
# task_detail = detail[['dishes_name','amounts']]
# detail_group = task_detail.groupby(by='dishes_name')
# print(detail_group.mean())
# print(detail_group.size().tail())

#2.agg---对于不同的列使用不同的聚合函数
#（1）一次性进行多个聚合统计
# a.所有列都执行聚合操作
lite_detail = detail[['counts','amounts']]
print('菜品销量和售价的均值:\n',lite_detail.agg([np.sum,np.mean]))

#b.指定列执行指定聚合操作
print('菜品销量总和 与 售价的均值:\n',lite_detail.agg({'counts':[np.sum,np.std],'amounts':np.mean}))

#c.可自定义聚合操作
def double_sum(col):
    return col*2

print('某上市公司为美化数据逼迫技术人员进行的数据分析操作:\n')
print(lite_detail.agg({'counts':double_sum},axis = 0))

print(detail[['counts','amounts']].agg(double_sum))

#apply
#每列均值
print('订单详情表的菜品销量与售价的均值:\n',detail[['counts','amounts']].apply(np.mean))

#每组均值
new_detail = detail[['order_id','counts','amounts']].groupby(by='order_id')
print(new_detail)#DataFrameGroupBy
# print('订单详情表中分组后每组的均值:\n',new_detail.apply(np.mean).head())
# print('订单详情表中分组后每组的标准差:\n',new_detail.apply(np.std).head())
#
# #transform
# print('订单详情表中菜品销量与售价的两倍:\n',detail[['counts','amounts']].transform(lambda x:2*x))
#
print('(分组后)订单详情表中菜品销量与售价的两倍:\n',new_detail.transform(lambda x:2*x))


#离差标准化:消除大单位和小单位的影响（消除量纲）变异大小的差异影响
# (当前值-最小值)/(最大值-最小值)

# def aa(x):
#     # print(type(x),x)#输出x是一个序列
#     fenzi = x-x.min()
#     fenmu = x.max() - x.min()
#
#     print(fenzi/fenmu)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('订单详情表分组后实现组内离差标准化:\n',new_detail.transform(lambda x:(x-x.min())/(x.max()-x.min()) ))


















