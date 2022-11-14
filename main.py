import numpy as np
import cv2
import utlis

utlis.initializeTrackbars()
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    count = 0
    _,img = cap.read()
    img = cv2.resize(img,(500,750))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thres = utlis.valTrackbars()
    imgThreshold = cv2.Canny(gray, thres[0], thres[1])
    cv2.imshow('imgT', imgThreshold)
    circles = cv2.HoughCircles(imgThreshold, cv2.HOUGH_GRADIENT, 1, 20,
                              param1=50, param2=30, minRadius=5, maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
            count += 1
    img = cv2.putText(img, "Point : {}".format(count), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                      (0, 0, 255), 1, cv2.LINE_AA, False)
    cv2.imshow('img', img)
    cv2.waitKey(1)