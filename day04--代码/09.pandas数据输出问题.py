import pandas as pd

#显示所有列
pd.set_option('display.max_columns',None)

#显示所有行
pd.set_option('display.max_rows',None)

#默认50，显示的长度
pd.set_option('max_colwidth',200)

#试试
detail = pd.read_excel('output.xlsx')
print(detail.head())