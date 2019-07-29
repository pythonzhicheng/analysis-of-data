import pandas as pd
import numpy as np

detail = pd.read_excel('meal_order_detail.xlsx')

#创建交叉表 （特殊透视表）
cross_table = pd.crosstab(index=detail['order_id'],
                columns=detail['dishes_name'],
                values=detail['counts'],
                aggfunc=np.sum
                )
print('以order_id行分组键、deshes_name为列分组键，得到到交叉表为：\n')
print(cross_table.head())

#
# 准备工作
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
date = [i.date() for i in detail['place_order_time']]
print(detail.shape)
detail['date'] = date
print(detail.shape)
# F = pd.ExcelWriter('output02.xlsx')
# detail.to_excel(F)
# F.save()



result =pd.crosstab(index=detail['date'],
            columns=detail['dishes_name'],
            values=detail['amounts'],
            aggfunc=np.sum,
            margins=True)
print(result.head())
print(type(result))
#
# F = pd.ExcelWriter('交叉表.xlsx')
# result.to_excel(F)
# F.save()

# 补强：
# loc
result = detail.loc[detail['order_id']==137,['dishes_name','amounts']]
print(result.head())

result = detail.loc[detail['amounts']>100,['dishes_name']]
print('菜品单价大于100元的数据：\n',result)

# iloc
# 格式：DataFrame.iloc[行索引位置, 列索引位置]

# print(detail.iloc[1,1])
# print(detail.iloc[0:6,1:6])






