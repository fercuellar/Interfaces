#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point, PointStamped
import ctypes

class GreenObjectDetector:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("camera/image_raw", Image, self.image_callback)
        self.coord_pub = rospy.Publisher("/green_object_coordinates", Point, queue_size=10)
        self.coord_pub_multiplier = rospy.Publisher('coordsx100', PointStamped, queue_size=10)

        self.point = PointStamped()
        self.point.header.frame_id = 'Camara'
        self.point.point.z = 0

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)
            return
        
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        
        lower_green = (40, 110, 40)
        upper_green = (80, 255, 200)    
        mask = cv2.inRange(hsv_image, lower_green, upper_green)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour
        
        if max_contour is not None:
            x, y, w, h = cv2.boundingRect(max_contour)
            cx = x + w/2
            cy = y + h/2
            
            green_point = Point()
            green_point.x = cx
            green_point.y = cy
            green_point.z = 0
            
            self.point.header.stamp = rospy.Time.now()

            x100 = ctypes.c_float(cx)
            y100 = ctypes.c_float(cy)
            z100 = ctypes.c_float(0)
            lib.multiply_coords(ctypes.pointer(x100),ctypes.pointer(y100),ctypes.pointer(z100))
            self.point.point.x = x100.value
            self.point.point.y = y100.value
            
            self.coord_pub_multiplier.publish(self.point)
            self.coord_pub.publish(green_point)
            
            # Dibujar contorno en la imagen original
            cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Mostrar imagen
        cv2.imshow("Green Object Detector", cv_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    lib = ctypes.CDLL("/home/fercuellar/Desktop/Robotica/catkin_ws/src/midterm/Scripts/libreria/libmy_library.so")

    rospy.init_node('green_object_detector', anonymous=True)
    green_detector = GreenObjectDetector()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
    cv2.destroyAllWindows()
