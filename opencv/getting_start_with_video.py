import cv2

#0 is for the number of camera
cap = cv2.VideoCapture(0)


# for saving the video we have to use fourcc code to store the video
fourcc =   cv2.VideoWriter_fourcc(*'XVID')
# 640 and 480 is a default frame of video
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    rat , frame = cap.read()
    if rat == True:
        # for geting frame of the video
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        out.write(frame)

        # if we want to video in black and white
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #pass gray instead of frame
        cv2.imshow('video',frame)


      # 0xFF is used for 64 bit device and ord is used to press the keywoard button if q is pressed then it will quit window 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
