import EM
import numpy as np
import cv2
from imutils import contours


cap = cv2.VideoCapture("detectbuoy.avi")

# points for GREEN (INSIDE)
# individualPixel = np.array([129, 242, 144])
# print(EM.getProbGMM(individualPixel, 'green'))
# individualPixel = np.array([119, 201, 119])
# print(EM.getProbGMM(individualPixel, 'green'))
# individualPixel = np.array([159, 240, 218])
# print(EM.getProbGMM(individualPixel, 'green'))
# individualPixel = np.array([128, 221, 146])
# print(EM.getProbGMM(individualPixel, 'green'))


# points for GREEN (INSIDE)
individualPixel = np.array([117, 181, 246])
#print(EM.getProbGMM(individualPixel, 'orange'))
individualPixel = np.array([113, 171, 247])
#print(EM.getProbGMM(individualPixel, 'orange'))
individualPixel = np.array([103, 153, 253])
#print(EM.getProbGMM(individualPixel, 'orange'))
individualPixel = np.array([107, 155, 251])
#print(EM.getProbGMM(individualPixel, 'orange'))
count = 0
while cap.isOpened():
	ret, frame = cap.read()

	out = frame.copy()
	rows, cols, _ = frame.shape
	binary = np.zeros((rows, cols, 3), np.float32)
	for i in range(rows):
		for j in range(cols):
			individualPixel = frame[i, j]
			temp = individualPixel[0]
			individualPixel[0] = individualPixel[2]
			individualPixel[2] = temp
			#print(i,"x",j,":",individualPixel)
			if (EM.getProbGMM(individualPixel, 'green') >= 3.00e-6):
				binary[i,j] = np.array([255,255,255])
			# else:
			#	 frame[i, j] = np.array([255, 255, 255])
	new = cv2.medianBlur(binary, 5)
	#new = cv2.GaussianBlur(new,(5,5),5)
	edges = cv2.Canny(np.uint8(new),50,255)
	conts,h = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	(conts_sorted, boundingBoxes) = contours.sort_contours(conts, method="left-to-right")
	hull = cv2.convexHull(conts_sorted[0])
	(x,y),radius = cv2.minEnclosingCircle(hull)
	if radius > 9:
		cv2.circle(out,(int(x),int(y)),int(radius),(0,255,0),4)

		#cv2.imshow("Final output",out)
		cv2.imwrite('output/'+str(count)+'.png', out)
		#images.append(out)
	else:
		#cv2.imshow("Final output",frame)
		cv2.imwrite('output/'+str(count)+'.png', out)
		#images.append(out)
	#cv2.imshow('frame',edges)
	count += 1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	#break
	# # When everything done, release the capture
	# cap.release()
	# cv2.destroyAllWindows()