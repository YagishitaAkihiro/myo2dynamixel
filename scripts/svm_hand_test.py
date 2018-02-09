#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.svm import LinearSVC
import numpy as np
import rospy
from myo2dynamixel.msg import EmgArray
from std_msgs.msg import Float64

class SVM_HC():
      def __init__(self):
          rospy.init_node("svm_hc")
          print "learning phase"
          # 学習データ
          data_training_tmp = np.loadtxt('/home/roboworks/catkin_ws/src/myo2dynamixel/scripts/data/train.txt', delimiter=',')
          data_training = [[x[1], x[2],x[3], x[4],x[5], x[6],x[7], x[8]] for x in data_training_tmp]
          label_training = [int(x[0]) for x in data_training_tmp]
          # 学習
          self.estimator = LinearSVC(C=1)#誤差項のペナルティパラメータC よくわからん。
          self.estimator.fit(data_training, label_training)
          print "starting node"
          self.pub = rospy.Publisher("/tilt_controller/command", Float64, queue_size=1)
          rospy.Subscriber("/myo_emg", EmgArray, self.call, queue_size=1)
          rospy.spin()

      def call(self,data):
          # 試験データ
          data_test = [[0,0,0,0,0,0,0,0]]
          for i in range(8):
              data_test[0][i] = data.data[i]
          
          # 予測するよー
          label_prediction = self.estimator.predict(data_test)
          if label_prediction == 1:
             print "開いてる"
             self.pub.publish(1)
          else:
             print "閉じてる"
             self.pub.publish(0.3)
#          print(label_prediction)
          rospy.sleep(0.2)

if __name__ == "__main__":
#   try:
     SVM_HC()
#   except:
#     print "error"
#参考ページ
#http://qiita.com/yasunori/items/8720c85e75b4679cae47
