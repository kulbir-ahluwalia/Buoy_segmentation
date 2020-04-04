import numpy as np
import matplotlib.pyplot as plt
from roipoly import roipoly as rp
import cv2
import pylab


# cap = cv2.VideoCapture("detectbuoy.avi")
#while cap.isOpened():
	#ret, frame = cap.read()
count = 1
for img in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]:
	
	frame = cv2.imread('frames/' + str(img) + '.png')
	
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	pylab.imshow(frame)
	roi = rp(roicolor='r')
	pylab.imshow(frame)
	###roi.displayROI()

	mask = roi.getMask(frame)
	#print(frame[100][100])
	output = np.zeros(frame.shape, np.uint8)
	
	for i in range(frame.shape[0]):
		for j in range(frame.shape[1]):
			if mask[i][j]:
				output[i][j][0] = frame[i][j][0]
				output[i][j][1] = frame[i][j][1]
				output[i][j][2] = frame[i][j][2]

	#cv2.imshow('output', output)
	print(img, count)

	cv2.imwrite(str(count) + '.png', output)
	count += 1

	# if cv2.waitKey(0) & 0xff == 27:	
	#  	break
	#  	cv2.destroyAllWindows()