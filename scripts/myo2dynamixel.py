#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import rospy
from std_msgs.msg import Float64
#from leap_motion.msg import leap
#from leap_motion.msg import leapros
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
#from common import *
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu
from std_msgs.msg import String, UInt8, Header, MultiArrayLayout, MultiArrayDimension, Float64MultiArray
from ros_myo.msg import MyoArm, EmgArray

pub = rospy.Publisher("/tilt_controller/command", Float64)

def send_command():
    rospy.init_node("myo_to_dynamixel")
#    rospy.Subscriber("/myo_emg", EmgArray, callback ,queue_size=10)    
#    rospy.Subscriber("/myo_emg", EmgArray, call)
    rospy.Subscriber("/myo_emg", EmgArray, catcher, queue_size=10)#要調整
    rospy.spin()

def call(data):
    print data.data[0]

def callback(data):	
    hnum = (data.data[0]/50)
    pub.publish(hnum)

def catcher(data):
    if data.data[0]>=200:
       print "I'm catching"
       pub.publish(0.2)#閉じるときの数値を入れて
    else:#if data.data[0]<100:
       print "I'm releasing"
       pub.publish(0.9)#開くときの数値を入れて

if __name__ == '__main__':
   send_command()
