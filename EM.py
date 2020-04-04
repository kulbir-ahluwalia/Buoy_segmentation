import numpy as np
import random


numModels = 2
weights = []
means = []
covs = []
for i in range(numModels):
	weights.append(1/numModels)
	means.append([])
	covs.append([])
	for j in range(3):
		means[i].append(random.randint(0,255))
		covs[i].append([])
		for k in range(3):
			covs[i][j].append(random.randint(0,255**2))
weights = np.array(weights)
means = np.array(means)
covs = np.array(covs)
# print(weights)
# print(means)
# print(covs)

'''
while(condition):
	alphas = np.array((numModels, numPixels))
	denoms = np.zeros(numPixles)
	for i in range(numModels):
		for j in range(numPixels):
			alphas[i][j] = weights[i]*prob(pixel_j|C_i)
			denoms[j] += alphas[i][j]

	for i in range(numModels):
		for j in range(numPixels):
			alphas[i][j] /= denoms[j]

	temp1 = temp2 = 0
	for i in range(numModels):
		for j in range(numPixels):
			temp1 += alphas[i][j]*x_j
			temp2 += alphas[i][j]*np.matmul((x_j - means[i]), (x_j - means[i]).transpose)
		s = np.sum(alphas[i])
		means[i] = temp1/s
		weights[i] = s/numPixels
		covs[i] = temp2/s


'''