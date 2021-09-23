import time
import numpy as np
import cv2
# Determining the codec type and creating the output file
codec=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter("InvisibilityCloak.avi",codec,20.0,(640,480))
camera=cv2.VideoCapture(0)
time.sleep(2)

bg=0
for i in range(60):
    ret,bg=camera.read()
bg=np.flip(bg,axis=1)

while (camera.isOpened()):
    ret,img=camera.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)

    lower_red=np.array([170,120,50])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)

    mask1=mask1+mask2

    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3), np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3), np.uint8))

    mask2=cv2.bitwise_not(mask1)

    res1=cv2.bitwise_and(img,img,mask=mask2)
    res2=cv2.bitwise_and(bg,bg,mask=mask1)

    final=cv2.addWeighted(res1,1,res2,1,0)
    output.write(final)



        
