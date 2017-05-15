#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.svm import LinearSVC
import numpy as np
import rospy
from myo2dynamixel.msg import EmgArray

class SVM_HC():
      def __init__(self):
          rospy.init_node("svm_hc")
          # 学習データ
          data_training_tmp = np.loadtxt('/home/aki/catkin_ws/src/myo2dynamixel/scripts/data/train.txt', delimiter=',')
          data_training = [[x[1], x[2],x[3], x[4],x[5], x[6],x[7], x[8]] for x in data_training_tmp]
          label_training = [int(x[0]) for x in data_training_tmp]
          rospy.Subscriber("/myo_emg", EmgArray, self.call, queue_size=1)
      def call(self,data):
          # 試験データ
          #data_test = np.loadtxt('/home/aki/catkin_ws/src/myo2dynamixel/scripts/data/Q.txt', delimiter=',')
          data_test = data.data()
          # 学習
          estimator = LinearSVC(C=0.88)#誤差項のペナルティパラメータC よくわからん。
          estimator.fit(data_training, label_training)

          # 予測するよー
          label_prediction = estimator.predict(data_test)
          if label_prediction == 1:
             print "開いてる"
          else:
             print "閉じてる"
          print(label_prediction)

if __name__ == "__main__":
#   try:
     SVM_HC()
#   except:
#     print "error"
#参考ページ
#http://qiita.com/yasunori/items/8720c85e75b4679cae47
