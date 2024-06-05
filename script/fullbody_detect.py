#!/usr/bin/env python3

#https://chantastu.hatenablog.com/entry/2022/09/11/002035#google_vignette

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
import time



# 体全体のカスケードファイル
cascade = cv2.CascadeClassifier("../data_xml/haarcascade_fullbody.xml")
#cascade = cv2.CascadeClassifier("/home/yamaguchi-a/catkin_ws/src/detect_pump/data_xml/haarcasca")



def image_callback(msg):
    bridge = CvBridge()
    try:
        #ROSのイメージメッセージをbgrのMat型に変換
        cv_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        fullbodyrect = cascade.detectMultiScale(cv_img)
        #print('FullBody Coordinate1:', fullbodyrect[0])

        if len(fullbodyrect) > 0:
            for [x,y,w,d] in fullbodyrect:
                cv2.rectangle(cv_img,(x,y),(x+w, y+d),(0,0,255),thickness=2)
        #cv_img = bridge.imgmsg_to_cv2(msg)  #ROSのイメージメッセージをMat型に変換

#######　処理を追加してみよう
        
        cv2.imshow("hogehoge", cv_img)
        cv2.waitKey(1)
        
    except Exception as e:
        print(e)



def main():
    rospy.init_node("camera_node")
    rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    rospy.spin()

if __name__ == "__main__":
    main()
