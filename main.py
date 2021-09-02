import numpy as np
import cv2

img1 = cv2.imread('tiger.jpg')
h,w,bpp = np.shape(img1)
img_gray =cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

img2=cv2.merge((img_gray,img_gray,img_gray))
th1, img3 = cv2.threshold(img2, 200,155, cv2.THRESH_BINARY)

scale_percent = 220 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)

dim = (width, height)

img4 = cv2.resize(img1,None,fx=0.1,fy=0.1, interpolation =cv2.INTER_AREA)

img4 = cv2.resize(img4,dim, interpolation =cv2.INTER_AREA)

img5 =cv2.GaussianBlur(img1,(3,3),0)

img6 =cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)


temp1 =np.concatenate((img1,img2,img3),axis=1)

temp2 =np.concatenate((img4,img6),axis=1)

#img_final =np.concatenate((temp1,temp2), axis=0)

cv2.imshow("result",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()