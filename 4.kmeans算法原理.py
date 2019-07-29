import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



##1.标准化数据：
##（1）小数定标标准化：
def data_trans(data):
    '''
    :param data:需要标准化的series
    :return:
    '''
    a = data/10**(np.ceil(np.log10(data.abs().max())))
    return a


def k_means(x_center, old_center, x):
    old_center = x_center.copy()
    #(2) 计算相似度：
    distance_arr = np.zeros((22, 3))##存放三个距离
    for index in range(x_center.shape[0]):
        distance = np.sqrt(np.sum((x - x_center[index])**2, axis=1))
        distance_arr[:, index] = distance
    sort_index = np.argmin(distance_arr, axis=1) ##分类结果；
    #(2) 更新类中心
    plt.figure()
    for i in range(3):
        ##求每类质心
        mask = sort_index == i
        x_result = x.loc[mask, :]
        y =x_result.mean(axis=0)

        x_center[i, :] = y
        ##可视化
        ##每类的点
        plt.scatter(x_result['平均消费周期（天）'], x_result['平均每次消费金额'])
        ##每类中心：
        plt.scatter(y[0], y[1], marker='*', s=30 )
    plt.show()

    return x_center, old_center

if __name__ == '__main__':
    data = pd.read_csv(r'company.csv', encoding='gbk')
    x = data.loc[:, ['平均消费周期（天）', '平均每次消费金额']]

    ##1.标准化：
    for i in x.columns:
        x[i] = data_trans(x[i])

    ##2.kmeans 算法：
    # (1) k = 3,初始化三个类中心：
    x_center = np.array([[0.01, 0.1], [0.02, 0.2], [0.03, 0.3]])   # 新的聚类中心
    old_center = np.array([[0.01, 0.1], [0.02, 0.2], [0.03, 0.3]]) #旧的聚类中心
    while True:
        x_center, old_center = k_means(x_center, old_center, x)
        print(x_center)
        # print(x_center==old_center)
        if (x_center == old_center).all():##np.all():逻辑与运算； np.any()逻辑或运算
            break















