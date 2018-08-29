
import os
import sys
import cv2
from libraries.background import BackGround

# By default the input is the web cam
# If otherwise stated the input is a video in location:
if __name__ == '__main__':
    myBackGround = BackGround()
    videoAddress = os.getenv('HOME') +'/trafficFlow/trialVideos'
    DEFAULT_WEBCAM_ADDRESS = 1
    videoInput = DEFAULT_WEBCAM_ADDRESS
    for input in sys.argv:
        if ('.mp4' in input) or ('.avi' in input):
            videoInput = videoAddress + '/' + input
            print('Input file: {}'.format(videoInput))

    if videoInput == DEFAULT_WEBCAM_ADDRESS:
        miCamara = cv2.VideoCapture(videoInput)
        miCamara.set(3,320)
        miCamara.set(4,240)
    else:
        miCamara = cv2.VideoCapture(videoInput)

    while True:
        succesfullyRead, flowFrame = miCamara.read()
        if videoInput != DEFAULT_WEBCAM_ADDRESS:
            flowFrame = cv2.resize(flowFrame,(320,240))

        rectangulos = myBackGround.getForeground(flowFrame)

        for rectangulo in rectangulos:
            #print(rectangulo)
            flowFrame = cv2.rectangle(flowFrame, rectangulo[0], rectangulo[1], (255,255,255), 1)
        #flowFrame = cv2.rectangle(flowFrame, (0,0), (25,25), (255,255,255), 1)
        cv2.imshow('Monitor',flowFrame)

        ch = 0xFF & cv2.waitKey(1)
        if ch == ord('q'):
            break
