#!/usr/bin/env python
#-*- coding:utf-8 -*-

def main():
    f=open("/home/roboworks/catkin_ws/src/myo2dynamixel/scripts/data/train.txt","w")
    for line in open("/home/roboworks/catkin_ws/src/myo2dynamixel/scripts/data/open.txt" , "r"):
        line = line.replace('(', '')
        line = line.replace(')', '')
        f.writelines("1, " + line)
    
    for line in open("/home/roboworks/catkin_ws/src/myo2dynamixel/scripts/data/close.txt", "r"):
        line = line.replace('(', '')
        line = line.replace(')', '')
        f.writelines("0, " + line)
    
    print("Finish!")
    f.close()

if __name__ == "__main__":
   main()
