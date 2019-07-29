import pandas as pd

#2.2.4
# (一)
detail = pd.read_excel('output.xlsx',sheetname=0)
print(detail.shape)
print(detail.ndim)
print(detail.size)

#(二)
detail['dishes_name'] = detail['dishes_name'].astype('category')
print('菜品以类型划分后的描述信息：\n',detail['dishes_name'].describe())

detail['order_id'] = detail['order_id'].astype('category')
print('订单以类型划分后的描述信息：\n',detail['order_id'].describe())



