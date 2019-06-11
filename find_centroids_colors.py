#!/usr/bin/python
from __future__ import print_function
from centroid_color import CentroidColor
import cv2 as cv
import json


variavel = open("dados.txt")
lines = variavel.readlines()
string = lines[0].strip()
biblio = json.loads(string)
color1 = CentroidColor(biblio)
window = 'Color Detection'
cv.namedWindow(window)

cap = cv.VideoCapture(0)
while True:
    ref, frame = cap.read()
    if frame is None:
        break
    cX, cY = color1.get_centroid(frame)
    frame_threshold = color1.get_frame_threshold(frame)
    if(cX is not None and cY is not None):
        cv.circle(frame_threshold, (cX, cY), 5, (0, 0, 0), -1)
        cv.putText(frame_threshold, "centroid", (cX - 25, cY - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    # cv.imshow(window, frame)
    cv.imshow(window, frame_threshold)
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
