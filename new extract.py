#!/usr/bin/env python

import os
import rospy
from sensor_msgs.msg import Image,CameraInfo
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped
from cv_bridge import CvBridge
import time

import cv2
import sys
import serial
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import String

processing= False
new_msg= True

class ArUco_Relay:

    def __init__(self,):
        # Create the subscriber for the topic from rosserial_python node to recieve the encoder data
        self.ROS_sub = rospy.Subscriber("/simple_aruco_detector/transforms", TransformStamped, self.Callback)
        self.ROS_pub = rospy.Publisher('/Pi/ArUco_ID', String, queue_size=10)
        self.ROS_msg = String()
        

    def Callback(self, data):
		ArUco_ID = data.child_frame_id
		global processing, new_msg
		if new_msg:
			#self.ROS_msg.data = ArUco_ID
			if ArUco_ID == "marker_id0":
				print('hello alan')
				os.system("say 'Hello Alan'")
				rate.sleep()
				new_msg=False
			elif ArUco_ID == "marker_id1":
				print('Hello Youssef')
				os.system("say 'Hello Youssef'") 
			elif ArUco_ID == "marker_id2":
				print('3 Hello Jonathan')
				os.system("say 'Hello Jonathan'")
			#	time.sleep(5)
			elif ArUco_ID == "marker_id3":
				print('Hello Sami')
				os.system("say 'Hello Sami'")
			#	time.sleep(5)
			elif ArUco_ID == "marker_id4":
				print('Hello Batel')
				os.system("say 'Hello Batel'")
			#	time.sleep(5)
			else: 
				print(ArUco_ID)
				#code goes here
		rate.sleep()	
		#new_msg=True
		self.ROS_msg.data = ArUco_ID

		
		#If ArUco_ID 1 is seen,
		# self.ROS_pub.publish(self.ROS_msgs)

if __name__ == '__main__':
    try:
        rospy.init_node('ArUco_Relay', anonymous=True)
        rate = rospy.Rate(0.2)
        Relay = ArUco_Relay()
        #Create Relay object and sleep until data from camera is published
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
