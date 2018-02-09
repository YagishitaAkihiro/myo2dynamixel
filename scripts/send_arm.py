#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function
import socket
import time
from contextlib import closing
import rospy
from std_msgs.msg import Float64

global angle_data
angle_data = ""

def callback(data):
    global angle_data
    angle_data = data.data
#    print (angle_data)
def main(host,port):
  hosts = host
  ports = port
  count = 0
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  rospy.Subscriber("/tilt_controller/command",Float64,callback,queue_size=1)
  with closing(sock):
    while not rospy.is_shutdown():
      global angle_data
#      print (angle_data)
      sock.sendto(str(angle_data), (hosts, ports))
      time.sleep(0.2)
  return

if __name__ == '__main__':
  rospy.init_node("hand_udp_send")
  host =  '10.254.21.23'
  port = 4001
  main(host,port)
