import pandas as pd
import numpy as np

#1.读文件：
data = pd.read_csv(r'C:\Users\ibm\Desktop\air_data.csv', encoding='gb18030', engine='python')
print(data.columns)
print(data.shape)
##处理特征值数据：
#(1)丢弃票价为空的记录。===>取出票价不为空的值：
mask_sum1 = data['SUM_YR_1'].notnull()
mask_sum2 = data['SUM_YR_2'].notnull()
mask_notnull = mask_sum1 & mask_sum2
data_notnull = data.loc[mask_notnull, :]
print(data_notnull.shape)

#(2)保留票价不为0，平均折扣率不为0，总飞行公里数大于0的记录。
mask1 = (data_notnull['SUM_YR_1'] !=0) | (data_notnull['SUM_YR_2'] !=0)
mask2 = data_notnull['avg_discount'] !=0
mask3 = data_notnull['SEG_KM_SUM'] > 0
mask_index = mask1 & mask2 & mask3
data_clear = data_notnull.loc[mask_index, :]
# print(data_clear.shape)

##2.提取特征： L	R	F	M	C
airline = data_clear[['FFP_DATE', 'LOAD_TIME', 'SEG_KM_SUM', 'avg_discount',  'FLIGHT_COUNT',  'LAST_TO_END']]
##构建L特征：
L = pd.to_datetime(airline['LOAD_TIME'])-pd.to_datetime(airline['FFP_DATE'])
# year = [i.year for i in (pd.to_datetime(airline['LOAD_TIME']))]
# year2 = [i.year for i in (pd.to_datetime(airline['FFP_DATE']))]
# print((np.array(year)-np.array(year2))*12)
# print(year)

L = (L/30).astype('str').str.split(' days ').str[0]

#最终特征值：
airline_feature = pd.concat([L, airline.iloc[:, 2:]], axis=1 )
print(airline_feature)

##标准化：
from sklearn.preprocessing import StandardScaler ##标准差标准化
data = StandardScaler().fit_transform(airline_feature)
print(data)

##k-means 算法：
from  sklearn.cluster import KMeans
##建模型
kmeans_model = KMeans(n_clusters= 5)
fit_kmeans = kmeans_model.fit(data)
print(fit_kmeans)

##聚类中心：
print(fit_kmeans.cluster_centers_)
##聚类标签：
print(fit_kmeans.labels_)
##每类有多少客户：
print(pd.Series(fit_kmeans.labels_).value_counts())


##可视化：雷达图：
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 6))

##闭合：
center = fit_kmeans.cluster_centers_
center_2 = center[:, 0].reshape((5, 1))

x_y = np.concatenate((center, center_2), axis=1)

##角度：
angles = np.linspace(0, 2*np.pi, 5, endpoint=False)
angles_b = np.concatenate((angles, [angles[0]]))

##绘图：
for i in range(5):
    plt.polar(angles_b, x_y[i], marker='*', linestyle=':')
    plt.fill(angles_b, x_y[i], alpha=0.25)
label = ['L', 'M', 'C', 'F', 'R']
plt.xticks(angles, label)
plt.show()




