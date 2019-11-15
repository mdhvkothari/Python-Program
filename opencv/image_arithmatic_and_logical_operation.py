import numpy as np
import cv2

#when both image have same scale and size

img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')

#we can add two images
add = img1+img2

#we can add like this
#add = cv2.add(img1,img2) but it will add pixels of both images

#we can added each image though its weight percentage
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
#this will give the 60% for image one and 40% of  image second and 0 is gamma value


cv2.imshow('image',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
