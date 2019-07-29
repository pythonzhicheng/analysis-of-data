
import pandas as pd

detail = pd.read_excel('output.xlsx')

#公共属性值
print(detail.shape)#(10037,19)
print(detail.size)#190703
print(detail.ndim)#2

#取一列数据
#格式：变量名['列名']
amounts = detail['amounts']
counts = detail['counts']
print(amounts)

#取多列数据
# 格式：变量名[['列名1','列名2',.....]]
detail_ac = detail[['amounts','counts']]
print('订单详情表中counts和amount两列的描述性统计信息为：\n',detail_ac.describe())

#关于行的读取
# 格式：变量名.loc[行,列]
detail_ac = detail.loc[:,['amounts','counts']]
print('读取数据：\n',detail_ac)


#类别处理
detail['order_id'] = detail['order_id'].astype('category')
detail['dishes_name'] = detail['dishes_name'].astype('category')

print('订单情况表中关于order_id(订单编号)'
      '与dishes_name(菜品名称)的描述性统计结果为：\n',detail[['order_id','dishes_name']].describe())


'''悬案
         order_id dishes_name
count      10037       10037
unique       942         159
top          398       白饭/大碗
freq          36         323

'''






