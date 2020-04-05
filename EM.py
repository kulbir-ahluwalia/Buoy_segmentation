import numpy as np
import random
import csv
import math

csv.field_size_limit(1000000000)

GREEN = {}
YELLOW = {}
ORANGE = {}


def generateCoVarMatrix(color):
    rows = color['CoVar_Mat'][1: -1].split(']')
    CoVarMatrix = np.array([rows[0][1:].split(','), rows[1][3:].split(','), rows[2][3:].split(',')], dtype=float)
    return CoVarMatrix


def generateMeanMatrix(color):
    return np.array([color['B_Mean'], color['G_Mean'], color['R_Mean']], dtype=float)


def generateProb(givenInt, coVarMat, meanPt):
    Det_CoVarMatrix = np.linalg.det(coVarMat)
    constant = 1 / (((2 * 3.14) ** 3) * Det_CoVarMatrix) ** (0.5)
    inv_CoVarMatrix = np.linalg.inv(coVarMat)
    ptMinMean = givenInt - meanPt
    e = np.matmul(np.matmul(ptMinMean, inv_CoVarMatrix), ptMinMean[:,None]) / (-2)
    # print(np.matmul(ptMinMean, inv_CoVarMatrix))
    return constant * math.exp(e)


reader = csv.reader(open('green.csv', 'r'))
for row in reader:
    if row == []:
        continue
    else:
        k, v = row
        GREEN[k] = v

reader = csv.reader(open('yellow.csv', 'r'))
for row in reader:
    if row == []:
        continue
    else:
        k, v = row
        YELLOW[k] = v

reader = csv.reader(open('orange.csv', 'r'))
for row in reader:
    if row == []:
        continue
    else:
        k, v = row
        ORANGE[k] = v

givenPt = np.array([[133], [230], [200]], dtype=float)

# CoVarMatrix_Green = generateCoVarMatrix(GREEN)
# meanPt_Green = generateMeanMatrix(GREEN)
# #print("probability that the intensity is green: ", generateProb(givenPt, CoVarMatrix_Green, meanPt_Green))

# CoVarMatrix_Yellow = generateCoVarMatrix(YELLOW)
# meanPt_Yellow = generateMeanMatrix(YELLOW)
# #print("probability that the intensity is yellow: ", generateProb(givenPt, CoVarMatrix_Yellow, meanPt_Yellow))

# CoVarMatrix_Orange = generateCoVarMatrix(ORANGE)
# meanPt_Orange = generateMeanMatrix(ORANGE)
# #print("probability that the intensity is orange: ", generateProb(givenPt, CoVarMatrix_Orange, meanPt_Orange))



pixels = []
with open('Dataset_generation/yellow_buoy_dataset.csv', mode='r') as file:
	reader = csv.reader(file, delimiter=',')
	for row in reader:
		pixels.append([int(row[0]), int(row[1]), int(row[2])])

numPixels = len(pixels)
pixels = np.array(pixels)
numModels = 5
threshold = []
weights = []
means = []
covs = []
for i in range(numModels):
	weights.append(1/numModels)
	means.append([])
	covs.append(generateCoVarMatrix(YELLOW))
	for j in range(3):
		means[i].append(random.randint(0,255))
		#covs[i].append([])
		#for k in range(3):
			#covs[i][j].append(random.randint(0,255))
weights = np.array(weights)
means = np.array(means)
#covs = [np.array(covs)]
#print(covs)
#covs = [generateCoVarMatrix(GREEN), generateCoVarMatrix(GREEN)]
#print(covs)

t = 11
while(t > 10):
	alphas = np.empty([numModels, numPixels])
	denoms = np.zeros(numPixels)
	for i in range(numModels):
		for j in range(numPixels):
			alphas[i][j] = weights[i]*generateProb(pixels[j], covs[i], means[i])
			#print(generateProb(pixels[j], covs[i], means[i]))
			denoms[j] += alphas[i][j]

	for i in range(numModels):
		for j in range(numPixels):
			alphas[i][j] /= denoms[j]

	temp1 = np.zeros(3)
	temp2 = np.zeros((3,3))
	oldmeans = means.copy()
	for i in range(numModels):
		for j in range(numPixels):
			temp1 += (alphas[i][j]*pixels[j]).reshape(3)
			diff = pixels[j] - means[i]
			temp2 += alphas[i][j]*(np.matmul([diff[:,None]], [diff])).reshape((3,3))

		s = np.sum(alphas[i])
		#print(alphas[i])
		if s:
			means[i] = temp1.copy()/s
			weights[i] = s/numPixels
			covs[i] = temp2.copy()/s

	res = []
	print(weights)
	for i in range(numModels):
		res.append(np.linalg.norm(means[i] - oldmeans[i]))
	t = sum(res)
	#print(res)
	#print(weights)
#print(means, weights)
