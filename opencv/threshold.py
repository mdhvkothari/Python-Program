import numpy as np
import cv2

img = cv2.imread('book.jpg')



retval , threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayScaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayScaled,12,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayScaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,1)


cv2.imshow('threshold',threshold)
cv2.imshow('GreyScale',threshold2)
cv2.imshow('Finally',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
