#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import rospy
from std_msgs.msg import Float64
import sys
import enum
import re
import struct
import sys
import threading
import time
import math
import serial
from serial.tools.list_ports import comports
from common import *
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu
from std_msgs.msg import String, UInt8, Header, MultiArrayLayout, MultiArrayDimension, Float64MultiArray
from myo2dynamixel.msg import MyoArm, EmgArray

pub = rospy.Publisher("/tilt_controller/command", Float64)

def send_command(mode):
    rospy.init_node("myo_to_dynamixel")
    if mode == 1:
       global f
       f = open("/home/roboworks/catkin_ws/src/myo2dynamixel/scripts/train.txt","w")
       rospy.Subscriber("/myo_emg", EmgArray, call, queue_size=1)
    else:
       rospy.Subscriber("/myo_emg", EmgArray, catcher, queue_size=1)#要調整
    rospy.spin()

def call(data):
    global f
    f.write(str(data.data)+"\n")
    print data.data

def catcher(data):
    if data.data[0]>=200:
       print "I'm catching"
       pub.publish(0.2)#閉じるときの数値を入れて
    else:#if data.data[0]<100:
       print "I'm releasing"
       pub.publish(0.9)#開くときの数値を入れて

if __name__ == '__main__':
   send_command(1) #mode 1:学習データ作るモード 2:制御モード
   global f
   f.close()
