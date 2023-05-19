#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def camera_publisher():
    """
    Función que publica imágenes de la cámara a través de ROS.
    """
    rospy.init_node('camera_publisher', anonymous=True)
    bridge = CvBridge()
    cap = cv2.VideoCapture(0)
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
    rate = rospy.Rate(10) # 10 Hz

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logwarn("Error al capturar la imagen desde la cámara")
            continue
        image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        image_pub.publish(image_msg)
    cap.release()

if __name__ == '__main__':
    try:
        print("Camera has been initialized, image running")
        camera_publisher()
        
    except rospy.ROSInterruptException:
        pass