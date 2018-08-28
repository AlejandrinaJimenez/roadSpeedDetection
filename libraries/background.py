import cv2

class BackGround():
    def __init__(self):
        self.fgbg = cv2.createBackgroundSubtractorMOG2()        # cv2.bgsegm.createBackgroundSubtractorGMG()
        #self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

    def getForeground(self,imagenActualEnRGB):
        imagenActualBS = cv2.cvtColor(imagenActualEnRGB,cv2.COLOR_BGR2GRAY)
        #fgmask = self.fgbg.apply(imagenActualBS)
        imagenActualBS = cv2.GaussianBlur(imagenActualBS,(11,11),0)
        #imagenActualBS = cv2.morphologyEx(imagenActualBS, cv2.MORPH_OPEN, self.kernel)
        fgmask = self.fgbg.apply(imagenActualBS)
        #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, self.kernel)

        _, contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        #fgmask = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
        #rectangulos = [cv2.boundingRect(contour) for contour in contours]
        rectangles = []
        for (index, contour) in enumerate(contours):
            contour = cv2.convexHull(contour)
            (x, y, w, h) = cv2.boundingRect(contour)
            if (h>36) or (w>24):
                rectangles.append([(x, y), (x+w, y+h)])
                #cv2.rectangle(fgmask, (x, y), (x+w, y+h), 255, 1)

        #cv2.imshow('BackGround',fgmask)
        #print(len(rectangles))
        return rectangles
