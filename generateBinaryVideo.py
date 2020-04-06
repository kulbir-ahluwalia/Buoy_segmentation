import EM
import numpy as np
import cv2


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
print(EM.getProbGMM(individualPixel, 'orange'))
individualPixel = np.array([113, 171, 247])
print(EM.getProbGMM(individualPixel, 'orange'))
individualPixel = np.array([103, 153, 253])
print(EM.getProbGMM(individualPixel, 'orange'))
individualPixel = np.array([107, 155, 251])
print(EM.getProbGMM(individualPixel, 'orange'))

while cap.isOpened():
    ret, frame = cap.read()

    rows, cols, _ = frame.shape
    for i in range(rows):
        for j in range(cols):
            individualPixel = frame[i, j]
            print(i,"x",j,":",individualPixel)
            if (EM.getProbGMM(individualPixel, 'green') >= 1.00e-5):
                frame[i,j] = np.zeros(3)
            else:
                frame[i, j] = np.array([255, 255, 255])
    cv2.imshow('frame',frame)
    if cv2.waitKey(100000) & 0xFF == ord('q'):
         break
    break
    # # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()