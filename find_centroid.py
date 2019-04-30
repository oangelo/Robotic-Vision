#!/usr/bin/python

from __future__ import print_function
import cv2 as cv
import argparse
import math as m
max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'
def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)
def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)
def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)
def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)
#parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
#parser.add_argument('--camera', help='Camera devide number.', default=0, type=int)
#parser.add_argument('--input', help='Path to input image.', default='../data/stuff.jpg')
#args = parser.parse_args()
cap = cv.VideoCapture(0)
#cap = cv.imread(args.input)
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)
cv.createTrackbar(low_H_name, window_detection_name , low_H, max_value_H, on_low_H_thresh_trackbar)
cv.createTrackbar(high_H_name, window_detection_name , high_H, max_value_H, on_high_H_thresh_trackbar)
cv.createTrackbar(low_S_name, window_detection_name , low_S, max_value, on_low_S_thresh_trackbar)
cv.createTrackbar(high_S_name, window_detection_name , high_S, max_value, on_high_S_thresh_trackbar)
cv.createTrackbar(low_V_name, window_detection_name , low_V, max_value, on_low_V_thresh_trackbar)
cv.createTrackbar(high_V_name, window_detection_name , high_V, max_value, on_high_V_thresh_trackbar)

on_low_H_thresh_trackbar(82)
on_high_H_thresh_trackbar(119)
on_low_S_thresh_trackbar(62)
on_high_S_thresh_trackbar(195)
on_low_V_thresh_trackbar(111)
on_high_V_thresh_trackbar(210)


l = 20
sq = int(l*m.sqrt(3)/3)
cXs = []
cYs = []
cXs1 = []
cYs1 = []
cXs2 = []
cYs2 = []
def centroid(i,thresh):
    cv.circle(thresh, (cXs[i],cYs[i]), 3, (255, 255, 255))
    cv.line(thresh, (cXs[i] - l, cYs[i] - sq),(cXs[i] + l,cYs[i] - sq),(0,0,0))
    cv.line(thresh, (cXs[i] + l, cYs[i] - sq),(cXs[i],cYs[i] + 2*sq),(0,0,0))
    cv.line(thresh, (cXs[i],cYs[i] + 2*sq),(cXs[i] - l,cYs[i] - sq),(0,0,0))

while True:
    ref, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    #frame_threshold = cv.inRange(frame_HSV, (95, 102,0),(126, 197,255))
    im2, contours, hierarchy = cv.findContours(frame_threshold,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_TC89_L1)
    if contours:
        len_max_c = len(counters)
        max_c_index = 0
        count = 0

    for c in contours:
        
        if(len(c) > len_max_c):
            max_c_index = count
            len_max_c = len(c)
        count += 1

        M = cv.moments(c)
        if M["m00"] != 0 :
            cX = int(M["m10"]/M["m00"])
            cY = int(M["m01"]/M["m00"])
            cXs.append(cX)
            cYs.append(cY)
        else:
            cX = 0
            cY = 0
            cXs.append(cX)
            cYs.append(cY)

    for i in range(len(cXs)):
        centroid(i,frame_threshold)

    cXs = []
    cYs = []

    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)
    cv.drawContours(frame,contours,max_c_index,(0,255,0),3)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break


