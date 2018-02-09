#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64

pub = rospy.Publisher("tilt_controller/command", Float64, queue_size = 1)

def callback(data):
    key_data = data.buttons
    if key_data[6] == 1:
       res_d = Float64()
       res_d.data = 0.0
       pub.publish(res_d)
    else:
       res_d = Float64()
       res_d.data = 1.0
       pub.publish(res_d)
#    print key_data[6]

def main():
    rospy.init_node("joy_hand")
    rospy.Subscriber("/joy", Joy, callback, queue_size = 1)
    rospy.spin()

if __name__ == "__main__":
   main()
