import picamera
from time import sleep

camera = picamera.PiCamera()
camera.capture('image.jpg')
