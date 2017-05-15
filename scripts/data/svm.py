#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.svm import LinearSVC
import numpy as np

# 学習データ
data_training_tmp = np.loadtxt('/home/aki/catkin_ws/src/myo2dynamixel/scripts/data/train.txt', delimiter=',')
data_training = [[x[1], x[2],x[3], x[4],x[5], x[6],x[7], x[8]] for x in data_training_tmp]
label_training = [int(x[0]) for x in data_training_tmp]

# 試験データ
data_test = np.loadtxt('/home/aki/catkin_ws/src/myo2dynamixel/scripts/data/Q.txt', delimiter=',')

# 学習
estimator = LinearSVC(C=0.88)#誤差項のペナルティパラメータC よくわからん。
estimator.fit(data_training, label_training)

# 予測するよー
label_prediction = estimator.predict(data_test)

print(label_prediction)

#参考ページ
#http://qiita.com/yasunori/items/8720c85e75b4679cae47
