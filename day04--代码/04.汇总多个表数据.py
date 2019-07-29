import pandas as pd
from pandas import DataFrame
import xlrd#pip install xlrd

wb =xlrd.open_workbook('meal_order_detail.xlsx')
sheets = wb.sheet_names()
print(sheets)

#总的数据容器
total = DataFrame()

#循环遍历所有sheet,汇总数据
for i in range(len(sheets)):
    data = pd.read_excel('meal_order_detail.xlsx',sheetname=i,index_col=False)
    print(data.shape[0])#<class 'pandas.core.frame.DataFrame'>

#     #汇总数据
#     total = total.append(data)
#
# print(total.shape)
#
# #保存
# writer = pd.ExcelWriter('output.xlsx')
# total.to_excel(writer,'Sheet1')
# writer.save()
#




