import os
import numpy as np
import pandas as pd


##所有训练集的文件名称==》返回列表：

def data_trans(path):
    dir_list = os.listdir(path)
    # print(dir_list)

    # 创建空的数组， 行为训练集个数， 列为1024个属性+1个标签=1025列
    arr = np.zeros((len(dir_list), 1025), dtype='int')

    ##读每个样本，目的还原数据：==》32*32的数组；
    for index_file, file_name in enumerate(dir_list):
        path_full = path + '\\' + file_name
        # print(path)
        data = np.loadtxt(path_full, dtype='str')
        # 还原原始小样本样式：
        arr_training = np.zeros((32, 32), dtype='int')
        for index, i in enumerate(data):
            arr_i = np.array(list(map(int, i)))
            arr_training[index] = arr_i

        ##大的样本数组中填充特征值，前1024列， 行对应的是第几个文件
        arr_ravel = arr_training.ravel()
        # print(arr_ravel.shape)
        arr[index_file, :-1] = arr_ravel
        ##大的样本数组中填充标签：
        label = int(file_name.split('_')[0])
        arr[index_file, -1] = label
    f_name = path.split('\\')[-1]
    np.savetxt(f'{f_name}.csv', arr, fmt='%d')
    return arr


if __name__ == '__main__':
    path_train = 'trainingDigits'
    path_test = 'testDigits'
    training_data = data_trans(path_train)
    test_data = data_trans(path_test)

    ##knn算法：
    k = 3
    lv = [0 for i in range(10)]
    for test in test_data:
        distance = np.sum((training_data[:, :-1] - test[:-1]) ** 2, axis=1)
        sorted_index = np.argsort(distance)[:k]
        predict_label = pd.Series(training_data[:, -1][sorted_index], dtype='int').mode()[0]
        real_label = test[-1]
        # print('真实值：', real_label)
        # print('预测值：', predict_label)
        if real_label != predict_label:
            lv[real_label] += 1
    for i in range(10):
        n = (test_data[:, -1] == i).sum()
        print((lv[i] / n))
