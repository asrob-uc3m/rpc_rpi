import cv2
import picamera

##Take image with Raspberry Pi camera
camera = picamera.PiCamera()
camera.capture('image.jpg')
camera.close()

##Load image
img = cv2.imread("image.jpg")

cv2.imshow("img",img)

cv2.waitKey(0)
