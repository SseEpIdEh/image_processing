import cv2
import numpy as np
img = cv2.imread('Flag_of_USA.jpg')
width=400
height=300
img1 = cv2.resize(img, (width, height))
kernel=np.ones((5,5),np.float32)/25              #an identity matrix 5*5  #1
dst=cv2.filter2D(img1,-1,kernel)                                          #2
cv2.imshow("dst",dst)
cv2.imshow("img1",img1)
kernel=np.ones((9,9),np.float32)/81             #an identity matrix 5*5
dst1=cv2.filter2D(img1,-1,kernel)
cv2.imshow("dst1",dst)
blur=cv2.blur(img1,(5,5))       #average filter:  #the result is the same way that used of 1 and 2 ways
cv2.imshow("blur",blur)




cv2.waitKey(0)
cv2.destroyAllWindows()