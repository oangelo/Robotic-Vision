import cv2 as cv

import json

class TrackBarWindow:
    def __init__(self, biblio):
        self.window_detection_name = "Track Bars"
        cv.namedWindow(self.window_detection_name)
        self.max_value = 255
        self.max_value_H = 255
        self.low_H = 0
        self.low_S = 0
        self.low_V = 0
        self.high_H = self.max_value
        self.high_S = self.max_value
        self.high_V = self.max_value
        self.low_H_name = 'Low H'
        self.low_S_name = 'Low S'
        self.low_V_name = 'Low V'
        self.high_H_name = 'High H'
        self.high_S_name = 'High S'
        self.high_V_name = 'High V'
        cv.createTrackbar(self.low_H_name, self.window_detection_name , biblio["LH"] , self.max_value_H, self.on_low_H_thresh_trackbar)
        cv.createTrackbar(self.high_H_name, self.window_detection_name , biblio["HH"], self.max_value_H, self.on_high_H_thresh_trackbar)
        cv.createTrackbar(self.low_S_name, self.window_detection_name , biblio["LS"], self.max_value, self.on_low_S_thresh_trackbar)
        cv.createTrackbar(self.high_S_name, self.window_detection_name , biblio["HS"], self.max_value, self.on_high_S_thresh_trackbar)
        cv.createTrackbar(self.low_V_name, self.window_detection_name , biblio["LV"], self.max_value, self.on_low_V_thresh_trackbar)
        cv.createTrackbar(self.high_V_name, self.window_detection_name , biblio["HV"], self.max_value, self.on_high_V_thresh_trackbar)
        self.on_low_H_thresh_trackbar(biblio["LH"])
        self.on_high_H_thresh_trackbar(biblio["HH"])
        self.on_low_S_thresh_trackbar(biblio["LS"])
        self.on_high_S_thresh_trackbar(biblio["HS"])
        self.on_low_V_thresh_trackbar(biblio["LV"])
        self.on_high_V_thresh_trackbar(biblio["HV"])


    def on_low_H_thresh_trackbar(self, val):
        self.low_H = val
        self.low_H = min(self.high_H-1, self.low_H)
        cv.setTrackbarPos(self.low_H_name, self.window_detection_name, self.low_H)

    def on_high_H_thresh_trackbar(self, val):
        self.high_H = val
        self.high_H = max(self.high_H, self.low_H+1)
        cv.setTrackbarPos(self.high_H_name, self.window_detection_name, self.high_H)

    def on_low_S_thresh_trackbar(self, val):
        self.low_S = val
        self.low_S = min(self.high_S-1, self.low_S)
        cv.setTrackbarPos(self.low_S_name, self.window_detection_name, self.low_S)

    def on_high_S_thresh_trackbar(self, val):
        self.high_S = val
        self.high_S = max(self.high_S, self.low_S+1)
        cv.setTrackbarPos(self.high_S_name, self.window_detection_name, self.high_S)

    def on_low_V_thresh_trackbar(self, val):
        self.low_V = val
        self.low_V = min(self.high_V-1, self.low_V)
        cv.setTrackbarPos(self.low_V_name, self.window_detection_name, self.low_V)

    def on_high_V_thresh_trackbar(self, val):
        self.high_V = val
        self.high_V = max(self.high_V, self.low_V+1)
        cv.setTrackbarPos(self.high_V_name, self.window_detection_name, self.high_V)

    def get_frame_threshold(self, frame):
        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        return (cv.inRange(frame_HSV, (self.low_H, self.low_S, self.low_V), (self.high_H, self.high_S, self.high_V)))

    def set_frame(self, frame):
        cv.imshow(self.window_detection_name, self.get_frame_threshold(frame))


if __name__ == '__main__':
    variavel = open("dados.txt")
    lines = variavel.readlines()
    string = lines[0].strip()
    biblio = json.loads(string)
    window_track = TrackBarWindow(biblio)
    cap = cv.VideoCapture(0)
    while True:
        ref, frame = cap.read()
        if frame is None:
            break
        window_track.set_frame(frame)
        key = cv.waitKey(30)
        if key == ord('q') or key == 27:
            break
