import numpy as np
import cv2

img = cv2.imread('watch.jpg',1)

#img[50:350,200:550] = [255,255,255]
watch_face = img[50:350,200:550]
img[0:300,0:350] = watch_face
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
