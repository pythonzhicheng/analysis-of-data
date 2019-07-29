import numpy as np

# 一、基本数据类型
# bool:由所在平台决定其精度的整数。int32、int64---字长
# int:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~。int32、int64
# 另外：int8\int16\int32\float32\float64...

#二、数据类型转换
# eg: float64\int32.....
#     np.float64(n)
# eg:
value1 = np.bool(10)
value2 = np.bool(0)
print(value1,value2)

#eg:
value3 = np.float64(True)
print(value3)

# 三、定义数据类型（数据存储结构）
# eg:
# 创建一个存储餐饮企业库存信息的数据类型。其中：
# （1）用一个长度为40个字符的字符串来记录商品名称
# （2）用一个64位的整数来记录商品的库存
# （3）用一个64位的单精度浮点数来记录商品的价格。
# (dataframe)
df = np.dtype([('name',np.str_,40),('numitems',np.int64),('price',np.float64)])
# items = np.array([('tomatoes',100,2),('cabbages',200,0.5),('apple',50,4.5)],dtype=df)
items = np.array([('tomatoestomatoestomatoestomatoestomatoestomatoestomatoestomatoestomatoestomatoes',100,2),('cabbages',200,0.5),('apple',50,4.5)],dtype=df)

print(items)

print(df['name'])#<U40
print(df['numitems'])#int64
print(type(df['name']))







