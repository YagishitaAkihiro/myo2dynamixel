from __future__ import print_function
import socket
from contextlib import closing
import rospy
from std_msgs.msg import Float64

pub = rospy.Publisher("/tilt_controller/command", Float64, queue_size=1)

def op_cl(boo):
    data = Float64()
    
    fl_id = float(boo)
    data.data = fl_id
    pub.publish(data)
def main():
  host = '127.0.0.1'
  port = 4001
  bufsize = 4096

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
    sock.bind((host, port))
    while not rospy.is_shutdown():
      op_cl(sock.recv(bufsize))
#      print(sock.recv(bufsize))
  return

if __name__ == '__main__':
   rospy.init_node("hand_udp_rec")
   main()
