import numpy as np
import random
import csv
import math
import yaml

from EM import *
from PIL import Image

import cv2

# Opens the Video file
cap = cv2.VideoCapture('./detectbuoy.avi')
import cv2

#to save the video
#night_ride is the instance of VideoWriter
buoy_detect = cv2.VideoWriter('night_ride.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (1920, 1080))

#to check if cap has some value
# print(cap.isOpened())
imgArray = []
while(cap.isOpened()):
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if ret == True:
        # Uncomment To find the frame width and height:-
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # # image_object is an object lol
        # try:
        #     image_object = Image.open(frame)
        # except IOError:
        #     pass

        # print(image_object.size)
        #image_array = np.array(image_object)
        image_array = np.array(frame)

        # print(image_array.shape)
        # image_array.shape = (480, 640, 3)

        depth_array = image_array.shape[0]  # 480, generally
        height_array = image_array.shape[1]  # 640, generally
        width_array = image_array.shape[2]  # 3, generally

        for i in range(depth_array):

            for j in range(height_array):


                    print("Pixel coord are: \n", "i: ",i,  "j: ",j)

                    #RGB
                    #getProbGMM([image_array[i][j][0], image_array[i][j][1], image_array[i][j][2]], 'green')

                    #BGR
                    getProbGMM([image_array[i][j][2], image_array[i][j][1], image_array[i][j][0]], 'green')







        cv2.imshow('frame_old', frame)
        imgArray.append(frame)


        #to quit video
        if cv2.waitKey(30) & 0xff == ord('q'):
            break


    else:
        break

for i in range(len(imgArray)):
    buoy_detect.write(imgArray[i])

cap.release()
buoy_detect.release()
cv2.destroyAllWindows()
# Runs till the end of the video































#
#
# # for generating dataset for orange buoy
# for img in range(1,28,1):
#
#     print(img)
#
#     path = 'orange_buoy_trimmed/' + str(img) + '.png'
#     print(path)
#
#     # image_object is an object lol
#     try:
#         image_object = Image.open(path)
#     except IOError:
#         pass
#
#     # print(image_object.size)
#     image_array = np.array(image_object)
#
#     #print(image_array.shape)
#     # image_array.shape = (480, 640, 3)
#
#     depth_array = image_array.shape[0]   #480, generally
#     height_array = image_array.shape[1]  #640, generally
#     width_array = image_array.shape[2]   #3, generally
#
#     for i in range(depth_array):
#
#         for j in range(height_array):
#
#             if (image_array[i][j][0]>0) or (image_array[i][j][1]>0) or (image_array[i][j][2]>0):
#                 row_contents = image_array[i][j]
#                 append_rows_in_csv_file('orange_buoy_dataset.csv', row_contents)
#
#



































