import io
import time
import picamera
import cv2
import numpy as np

loop=True
# Create the in-memory stream
stream = io.BytesIO()
camera = picamera.PiCamera()

while(1):
#	camera.start_preview()
	#time.sleep(5)
	camera.capture(stream, 'jpeg')
	#camera.stop_preview()

# construct a numpy array from the stream
	data = np.fromstring(stream.getvalue(),dtype=np.uint8)
# decode the image from the array , preserving colour
	image = cv2.imdecode(data,1)
# opencv returns an array with data in BRG order. if you want RGB instead
# use the following ...
#	image = image[:, :, ::-1]
	cv2.imshow("stream",image)
	if cv2.waitKey(5) == 27:
		break
#	if k == '\x1b':
#		loop=False
camera.close()
cv2.destroyAllWindows()
