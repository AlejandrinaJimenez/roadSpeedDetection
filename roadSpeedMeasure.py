
import os
import sys
import cv2

# By default the input is the web cam
# If otherwise stated the input is a video in location:
if __name__ == '__main__':
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
        succesfullyRead, frameFlujo = miCamara.read()
        if videoInput != DEFAULT_WEBCAM_ADDRESS:
            frameFlujo = cv2.resize(frameFlujo,(320,240))

        cv2.imshow('Monitor',frameFlujo)

        ch = 0xFF & cv2.waitKey(1)
        if ch == ord('q'):
            break
