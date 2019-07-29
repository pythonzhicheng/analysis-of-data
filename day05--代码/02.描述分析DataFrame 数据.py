import pandas as pd

detail = pd.read_excel('output.xlsx',sheetname=0)

#求一共买出去多少份菜
# print(detail['counts'].sum())

cols  = detail.columns
# print(cols,type(cols))

# 同一行语句在不同的版本得到的数据类型是不一样的。
# for col in cols:
#     if isinstance(detail[col],object):
#         print(detail[col].dtypes)
#     if detail[cols].dtyps
#     print(detail[col].std())



