# PIL = Python imaging library
# It provides the python interpreter with image editing capabilities
from PIL import Image
import numpy as np
from csv import writer


def append_rows_in_csv_file(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

# for generating dataset for orange buoy
for img in range(1,28,1):
    print(img)

    path = 'orange_buoy_trimmed/' + str(img) + '.png'
    print(path)

    # image_object is an object lol
    try:
        image_object = Image.open(path)
    except IOError:
        pass

    # print(image_object.size)
    image_array = np.array(image_object)

    #print(image_array.shape)
    # image_array.shape = (480, 640, 3)

    depth_array = image_array.shape[0]   #480, generally
    height_array = image_array.shape[1]  #640, generally
    width_array = image_array.shape[2]   #3, generally

    for i in range(depth_array):

        for j in range(height_array):

            if (image_array[i][j][0]>0) or (image_array[i][j][1]>0) or (image_array[i][j][2]>0):
                row_contents = image_array[i][j]
                append_rows_in_csv_file('orange_buoy_dataset.csv', row_contents)




# for generating dataset for green buoy
for img in range(1,40,1):
    print(img)

    path = 'green_buoy/' + str(img) + '.png'
    print(path)

    # image_object is an object lol
    try:
        image_object = Image.open(path)
    except IOError:
        pass

    # print(image_object.size)
    image_array = np.array(image_object)

    print(image_array.shape)
    # image_array.shape = (480, 640, 3)

    depth_array = image_array.shape[0]   #480, generally
    height_array = image_array.shape[1]  #640, generally
    width_array = image_array.shape[2]   #3, generally

    for i in range(depth_array):

        for j in range(height_array):

            if (image_array[i][j][0]>0) or (image_array[i][j][1]>0) or (image_array[i][j][2]>0):
                row_contents = image_array[i][j]
                append_rows_in_csv_file('green_buoy_dataset.csv', row_contents)




# for generating dataset for yellow buoy
for img in range(1,31,1):
    print(img)

    path = 'yellow_buoy/' + str(img) + '.png'
    print(path)

    # image_object is an object lol
    try:
        image_object = Image.open(path)
    except IOError:
        pass

    # print(image_object.size)
    image_array = np.array(image_object)

    print(image_array.shape)
    # image_array.shape = (480, 640, 3)

    depth_array = image_array.shape[0]   #480, generally
    height_array = image_array.shape[1]  #640, generally
    width_array = image_array.shape[2]   #3, generally

    for i in range(depth_array):

        for j in range(height_array):

            if (image_array[i][j][0]>0) or (image_array[i][j][1]>0) or (image_array[i][j][2]>0):
                row_contents = image_array[i][j]
                append_rows_in_csv_file('yellow_buoy_dataset.csv', row_contents)




























































































































































































#     # List of strings
#     row_contents = [32, 'Shaun', 'Java', 'Tokyo', 'Morning']
#     # Append a list as new line to an old csv file
#     append_rows_in_csv_file('students.csv', row_contents)
#
#
#
#
#
#
#
#
#
# for img in range(1,31,1):
#
#     path = 'orange/' + str(img) + '.png'
#
#
#     # image_object is an object lol
#     try:
#         image_object = Image.open(path)
#     except IOError:
#         pass
#
#     #frame = cv2.imread(path)
#
#     #we use a function of Image module called getdata() to extract the pixel values
#     #it scans the image horizontally from left to right starting at the top-left corner
#     #The values got from each pixel is then added into a list
#     #what we get is a list with each pixel value as a set of 4 values(R,G,B,A)
#     #pixel_values is a list of sets
#     #pixel_values = list(image_object.getdata())
#     # width, height = image_object.size
#
#     # print(image_object.size)
#     image_array = np.array(image_object)
#
#     # print(image_array[240])          #prints the entire 2by2 matrix at 240th index
#     # print(image_array[240][499])     #prints the 240th index matrix's 499 index row
#     # print(image_array[240][499][1])  #prints that row's element at index 1
#
#     # print(image_array)
#     print(image_array.shape)
#
#
#
#     for i in range(image_array.shape[0]):
#
#
#
#         np.savetxt("pixel_data" + str(i) + ".csv", image_array[i], delimiter=",")
#
#
#
#
#
#
# #
# # path = 'orange/28.png'
# # # path = 'lenas_oranges/28.png'
# # # path = 'orange/' + '5' + '.png'
# # print(path)
# #
# # # image_object is an object lol
# # try:
# #     image_object = Image.open(path)
# # except IOError:
# #     pass
# #
# # #print(image_object.size)
# # image_array = np.array(image_object)
# #
# # # print(image_array[240])          #prints the entire 2by2 matrix at 240th index
# # # print(image_array[240][499])     #prints the 240th index matrix's 499 index row
# # # print(image_array[240][499][1])  #prints that row's element at index 1
# #
# # #print(image_array)
# #
# # print(image_array.shape)
# #
# #
# #
# #
# # #pixel_values = list(image_object.getdata())
# #
# #
# #  #pixels = np.asarray(pixel_values)
# # #np.savetxt("pixel_data.csv", pixels, delimiter=",")
# #
# # #print(pixel_values)
# #
# #
# #
# #
# #
# #
# #
# # #
# #
# # #
# # #     print(pixel_values)
# # #
# # #
# # #    #print(pixel_values_flat)
# # #
# # #
# # #
# # #
# # #
