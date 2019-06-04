import cv2 as cv

class CenroidColor:
    def __init__(self, color_list):
        self.color_list = color_list["LH"]

    def get_centroid(frame):
        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        frame_threshold = cv.inRange(frame_HSV, (self.color_list["LH"], self.color_list["LS"], self.color_list["LV"]), (self.color_list["HH"], self.color_list["HS"], self.color_list["HS"]))
        contours, hierarchy  = cv.findContours(frame_threshold,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_TC89_L1)
        if contours:
            len_max_c = len(contours[0])
            max_c_index = 0;
            count = 0
        for c in contours:
            if(len(c) > len_max_c):
                max_c_index = count
                len_max_c = len(c)
            count += 1
            M = cv.moments(c)
            if M["m00"] != 0 :
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = 0, 0
