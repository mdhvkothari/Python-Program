import numpy as np
import cv2

img1 = cv2.imread('1.png')
img2 = cv2.imread('logo.png')

#now we wanna join two different image at top left of image1

row,col,channels = img2.shape
#region of image
roi = img1[0:row,0:col]

#change image  into grey
img2grey = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# we are gonna apply threshold
#In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255)
ret,mask = cv2.threshold(img2grey,220,225,cv2.THRESH_BINARY_INV)
#here if any pixel value is greater than 220 then it will convert into 225 which is white and which is less than 220 it will convert into black
#and THRESH_BINARY_INV is do opposite of that change black into white and white into black
#cv2.imshow('mask',mask)

mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('mask_inv',mask_inv)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:row,0:col] = dst

cv2.imshow('res',img1)





cv2.waitKey(0)
cv2.destroyAllWindows()
