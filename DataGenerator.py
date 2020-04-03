import cv2
import numpy as np
import csv

B_DataSet = []
G_DataSet = []
R_DataSet = []

for pic in range(1, 40, 1):
    img = cv2.imread('green/' + str(pic) + '.png')
    rows, cols, _ = img.shape
    for i in range(rows):
        for j in range(cols):
            k = img[i, j]
            if (np.zeros(3) != k).all():
                B_DataSet.append(k[0])
                G_DataSet.append(k[1])
                R_DataSet.append(k[2])

B_Mean = np.mean(B_DataSet)
G_Mean = np.mean(G_DataSet)
R_Mean = np.mean(R_DataSet)

meanPt = np.array([[B_Mean], [G_Mean], [R_Mean]], dtype=float)

# B_SD = np.std(B_DataSet)
# G_SD = np.std(G_DataSet)
# R_SD = np.std(R_DataSet)

finalMat = np.zeros((3,3))
for i in range(len(B_DataSet)):
    mat1 = np.array([[B_DataSet[i]], [G_DataSet[i]], [R_DataSet[i]]], dtype=float) - meanPt
    mat2 = np.transpose(mat1)
    finalMat += np.matmul(mat1, mat2)
finalMat = np.divide(finalMat, len(B_DataSet))

# co_Var_Matrix = np.array([[B_SD**2, B_SD*G_SD, B_SD*R_SD], [B_SD*G_SD, G_SD**2, G_SD*R_SD], [B_SD*R_SD, G_SD*R_SD, R_SD**2]], dtype=float)
Green = {"B_intensities": B_DataSet, "G_intensities": G_DataSet, "R_intensities": R_DataSet, "B_Mean": B_Mean, "G_Mean": G_Mean, "R_Mean": R_Mean, "CoVar_Mat": finalMat.tolist()}
w = csv.writer(open("green.csv", "w"))
for key, val in Green.items():
    w.writerow([key, val])
