#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image,CameraInfo
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped
from cv_bridge import CvBridge

#import airsim
import cv2
#import numpy as np here
import sys
import serial
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import String

class ArUco_Relay:

    def __init__(self,):
        # Create the subscriber for the topic from rosserial_python node to recieve the encoder data
        self.ROS_sub = rospy.Subscriber("/simple_aruco_detector/transforms", TransformStamped, self.Callback)
        self.ROS_pub = rospy.Publisher('/Pi/ArUco_ID', String, queue_size=10)
        self.ROS_msg = String()

    def Callback(self, data):
        ArUco_ID = data.child_frame_id
        #If ArUco_ID 1 is seen,
        #if ArUco_ID == "ArUco_ID 1":
            #Do something
	print(ArUco_ID)
            #code goes here

        self.ROS_msg.data = ArUco_ID
       # self.ROS_pub.publish(self.ROS_msgs)

if __name__ == '__main__':
    try:
        rospy.init_node('ArUco_Relay', anonymous=True)
        rate = rospy.Rate(100)
        Relay = ArUco_Relay()
        #Create Relay object and sleep until data from camera is published
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
