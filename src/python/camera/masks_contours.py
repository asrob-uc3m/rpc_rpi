import cv2
import numpy as np

original_im = cv2.imread("objects01.png")
im = cv2.imread("objects01.png")
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for h,cnt in enumerate(contours):
	mask = np.zeros(imgray.shape,np.uint8)
	cv2.drawContours(mask,[cnt],0,255,-1)
	mean = cv2.mean(im,mask = mask)

cv2.imshow("img",mask)

cv2.imshow("original_img",original_im)
cv2.waitKey(0)
