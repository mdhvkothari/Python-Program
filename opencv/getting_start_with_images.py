import cv2
# we have to pass an extra parameter in which we want to read an image
# 0 for loads image in grey scale mode
# 1 for loads as color image
# -1 loads image as such including alpha channel
img = cv2.imread('lena.jpg',0)
print(img)
# how to see the image
# 'image' is the window name
cv2.imshow('image',img)
#wait for any key to press
cv2.waitKey(0)
cv2.destroyAllWindows()
