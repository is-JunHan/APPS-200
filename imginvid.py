import cv2
import numpy as np
import datetime
import math
import os
import sys
from matplotlib import pyplot as plt

def process_img(img_rgb, template, timestamp, inputVideo):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)

    #loops for every matching frame
    for pt in zip(*loc[::-1]):
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2) #draws rectangle of matching point
        #cv2.imshow('Match', img_rgb) #displays frame

        #finds the timestamp of the first matched frame
        cutTime = datetime.timedelta(milliseconds=timestamp)
        totalSeconds = cutTime.total_seconds()
        cutTime = datetime.timedelta(seconds = (math.ceil(totalSeconds) - 1))

        #trims video to the point of first matched frame
        cut_video = "ffmpeg -i "+ inputVideo + " -ss 00:00:00 -to 0" + str(cutTime) + " -c:v copy -c:a copy output.mp4"
        os.system(cut_video)
        sys.exit("video cut")

def main():
    inputVideo = sys.argv[1]

    #loads inputVideo using opencv library
    vidcap = cv2.VideoCapture(inputVideo)
    
    #skips video for faster testing. Remove in production. 
    vidcap.set(cv2.CAP_PROP_POS_MSEC,144000) 

    # template is the 'needle' frame that we are looking for in the video
    template = cv2.imread('bars.png',0)  
    count = 0
    #loops through all frames in inputVideo / vidcap
    while True:
      success,image = vidcap.read()
      if not success: break        
      print ('Read a new frame: ', count)
      count += 1
      #returns timestamp of current frame in milliseconds 
      timestamp = vidcap.get(cv2.CAP_PROP_POS_MSEC) 
      print ('Read a new frame: ', count)
      process_img(image, template, timestamp, inputVideo)
      


if __name__ == "__main__":
    main()