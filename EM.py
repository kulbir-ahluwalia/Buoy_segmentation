import numpy as np
import random
import csv
import math
import yaml

csv.field_size_limit(1000000000)
GMM_Global = {}


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
    e = np.matmul(np.matmul(ptMinMean, inv_CoVarMatrix), ptMinMean[:, None]) / (-2)
    # print(np.matmul(ptMinMean, inv_CoVarMatrix))
    return constant * math.exp(e)


def getGMM(colorClass):
    DICT = {}

    reader = csv.reader(open(colorClass + '.csv', mode='r'))
    for row in reader:
        if row == []:
            continue
        else:
            k, v = row
            DICT[k] = v

    reader = csv.reader(open(colorClass + '.csv', mode='r'))
    for row in reader:
        if row == []:
            continue
        else:
            k, v = row
            DICT[k] = v

    reader = csv.reader(open(colorClass + '.csv', mode='r'))
    for row in reader:
        if row == []:
            continue
        else:
            k, v = row
            DICT[k] = v

    pixels = []
    with open('Dataset_generation/' + colorClass + '_buoy_dataset.csv', mode='r') as file:
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
        weights.append(1 / numModels)
        means.append([])
        covs.append(generateCoVarMatrix(DICT))
        for j in range(3):
            means[i].append(random.randint(0, 255))
        # covs[i].append([])
        # for k in range(3):
        # covs[i][j].append(random.randint(0,255))
    weights = np.array(weights)
    means = np.array(means)

    t = 11
    while (t > 10):
        alphas = np.empty([numModels, numPixels])
        denoms = np.zeros(numPixels)
        for i in range(numModels):
            for j in range(numPixels):
                alphas[i][j] = weights[i] * generateProb(pixels[j], covs[i], means[i])
                # print(generateProb(pixels[j], covs[i], means[i]))
                denoms[j] += alphas[i][j]

        for i in range(numModels):
            for j in range(numPixels):
                alphas[i][j] /= denoms[j]

        temp1 = np.zeros(3)
        temp2 = np.zeros((3, 3))
        oldmeans = means.copy()
        for i in range(numModels):
            for j in range(numPixels):
                temp1 += (alphas[i][j] * pixels[j]).reshape(3)
                diff = pixels[j] - means[i]
                temp2 += alphas[i][j] * (np.matmul([diff[:, None]], [diff])).reshape((3, 3))

            s = np.sum(alphas[i])
            # print(alphas[i])
            if s:
                means[i] = temp1.copy() / s
                weights[i] = s / numPixels
                covs[i] = temp2.copy() / s

        res = []
        print(weights)
        for i in range(numModels):
            res.append(np.linalg.norm(means[i] - oldmeans[i]))
        t = sum(res)

    data = dict(
        weights={},
        means={},
        covMats={},
    )

    for i in range(numModels):
        data['weights'][i] = float(weights[i])
        data['means'][i] = {}
        data['covMats'][i] = {}
        for j in range(3):
            data['means'][i][j] = float(means[i][j])
            data['covMats'][i][j] = {}
            for k in range(3):
                data['covMats'][i][j][k] = float(covs[i][j][k])

    with open(colorClass + '_GMM.yaml', mode='w') as file:
        yaml.dump(data, file)


def getProbGMM(currPixel, colorClass):
    if GMM_Global.get(colorClass, None) == None:
        with open(colorClass + '_GMM.yaml', mode='r') as file:
            GMM = yaml.safe_load(file)

        covs = []
        means = []
        for i in range(len(GMM['weights'])):
            means.append([])
            covs.append([])
            for j in range(3):
                means[i].append(GMM['means'][i][j])
                covs[i].append([])
                for k in range(3):
                    covs[i][j].append(GMM['covMats'][i][j][k])
        GMM_Global[colorClass] = {}
        GMM_Global[colorClass]['length'] = len(GMM['weights'])
        GMM_Global[colorClass]['means'] = np.array(means)
        GMM_Global[colorClass]['covs'] = np.array(covs)

    # print(means, covs)
    p = 0
    for i in range(GMM_Global[colorClass]['length']):
        p += generateProb(currPixel, GMM_Global[colorClass]['covs'][i], GMM_Global[colorClass]['means'][i])

    return (p)

# -----------------------------------------------------------------------------------------------------
# HOW TO USE: getProbGMM([1, 1, 1], 'green')
# -----------------------------------------------------------------------------------------------------
# getGMM('orange')
# print(GMM)
