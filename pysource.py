import cv2 as cv
import numpy as np
import cv2.aruco
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

# cv.imshow('image',image)
from object_detector import *
detector = HomogeneousBgDetector()
image = cv.imread('images.jfif')
cv.imshow("Original Image",image) 
corners, _, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)
int_corners = np.int0(corners)
cv.polylines(image,int_corners,True,(155,125,77),2)

print(corners)
contours = detector.detect_objects(image)
print(contours)
for cnt in contours:
    # cv.polylines(image,[cnt],True,(0,255,0),2)
    rect = cv.minAreaRect(cnt)
    (x,y),(w,h),angle = rect
    # cv.circle(image,(int(x),int(y)),5,(0,255,0),-1)
    # print(x,y)
    # print(w,y)
    # print(angle)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.circle(image,(int(x),int(y)),5,(0,255,0),-1)
    # box = np.int0(0)
    # cv.polylines(image,[box],True,(0,255,0),2)7
    cv.polylines(image,[box],True,(0,255,0),2)
    cv.putText(image,'width {}'.format(round(w,1)),(int(x),int(y-100)),cv.FONT_HERSHEY_PLAIN,1,(255,0,255))
    cv.putText(image,'height {}'.format(round(h,1)),(int(x),int(y+100)),cv.FONT_HERSHEY_PLAIN,1,(255,0,255))
    print(box)

cv.imshow('imgae',image)
cv.waitKey(0)

import pickle
pickle.dump(image,open('model1.pkl','wb'))