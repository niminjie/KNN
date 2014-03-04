from numpy import *
import kdTree
import datetime
import time
import operator
import math
import os
import sys

trainPath = '/Users/niminjie/Documents/workspace/PythonSrc/KNN/dataset/synth.te'
testPath = '/Users/niminjie/Documents/workspace/PythonSrc/KNN/dataset/synth.tr'

def dieWithUsage():
    print u'''
|***********************How to use Neual Networds******************************|
|  Example: python KNN.py <trainPath> <testPath>                         |
|******************************************************************************|
|  Flags:                                                                      |
|  -help        Display how to use the script                                  |
|------------------------------------------------------------------------------|
|  Parameters:                                                                 |
|  trainPath    Train data path                                                |
|  testPath     Test data path                                                 |
|------------------------------------------------------------------------------|
'''
    sys.exit(0)

def getParams():
    global trainPath
    global testPath

    if len(sys.argv) == 1:
        return 0

    if len(sys.argv) == 2:
        print '-------------------------------------------------'
        print '******ERROR:Please input enough parameters!******'
        print '-------------------------------------------------'
        dieWithUsage()

    if sys.argv[1].lower() == '-help':
        dieWithUsage()

    # Get flags
    while True:
        if sys.argv[1].lower() == '-flag1':
            pass
        if sys.argv[2].lower() == '-flag2':
            pass
        else:
            break
        sys.argv.pop(1)

    # Get params
    trainPath = sys.argv[1]
    # print trainPath
    testPath = sys.argv[2]
    # print testPath
    if not os.path.exists(trainPath):
        print 'Train set: %s not found!!' %trainPath
    if not os.path.exists(testPath):
        print 'Test set: %s not found!!' %testPath

def readFile(trainPath, testPath, head = False):
    trainSet, testSet = [], []
    trainLabel, testLabel = [], []

    for line in open(trainPath, 'r'):
        row = convertToDouble(line.strip().split()[0:2])
        trainSet.append(row)
        # if len(line.strip().split()) >= 3 and isNum(line.strip().split()[2]):
        if isNum(line.strip().split()[2]):
            trainLabel.append(float(line.strip().split()[2]))

    for line in open(testPath, 'r'):
        row = convertToDouble(line.strip().split()[0:2])
        testSet.append(row)
        # if len(line.strip().split()) >= 3 and isNum(line.strip().split()[2]):
        if isNum(line.strip().split()[2]):
            testLabel.append(float(line.strip().split()[2]))

    if head == False:
         return trainSet[1:], testSet[1:], trainLabel, testLabel
    else:
         return trainSet, testSet, trainLabel, testLabel


def fileToDict(trainPath, testPath, head = False):
    trainSet, testSet= {}, {}

    for line in open(trainPath):
        flag = False
        for i in line.strip().split():
            if not isNum(i):
                flag = True
        if flag == True:
            continue
        key = tuple(convertToDouble(line.strip().split()[0:2]))
        value = int(line.strip().split()[-1])
        trainSet.setdefault(key, value)

    for line in open(testPath):
        flag = False
        for i in line.strip().split():
            if not isNum(i):
                flag = True
        if flag == True:
            continue
        key = tuple(convertToDouble(line.strip().split()[0:2]))
        value = int(line.strip().split()[-1])
        testSet.setdefault(key, value)
    return trainSet, testSet

def makeMatrix(trainSet, testSet):
    trainMatrix = array(trainSet)
    testMatrix = array(testSet)
    return trainMatrix, testMatrix

def convertToDouble(strData):
    return [float(d) for d in strData if isNum(d)]

def isNum(value):
    try:
        float(value)
    except ValueError:
        return False
    else:
        return True

def precision(result, target):
    if len(result) != len(target):
        print 'Result and target length must equal'
        return 0
    hits = 0
    for i in range(len(result) - 1):
        if result[i] == target[i]:
            hits += 1
    return hits * 1.0 / len(result)


def classify0(inX, dataSet, labels, k):
    # Matrix row number
    dataSetSize = dataSet.shape[0]
    '''
    >>> np.tile(a, (2, 2))
    array([[0, 1, 2, 0, 1, 2],
       [0, 1, 2, 0, 1, 2]])
    '''
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # Every element in the matrix ** 2
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        # print sortedDistIndicies[i]
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    #print classCount
    # Itemgetter: Get 1th value(index starts with 0)
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def classifyKdTree(inX, trainSet, k = 1):
    tree = kdTree.createTree(trainSet.keys())
    nearest = kdTree.searchTree(tree, inX, k)
    print nearest

def main():
    getParams()
    # readFile(trainPath, testPath)
    # trainSet, testSet, trainLabel, testLabel = readFile(trainPath, testPath)
    # trainMatrix, testMatrix = makeMatrix(trainSet, testSet)
    trainSet, testSet = fileToDict(trainPath, testPath)
    # print testSet
    # print len(trainLabel)
    # print len(testLabel)
    # for k in range(1, 31):
    #     result = [classify0(row, trainMatrix, trainLabel, k) for row in testMatrix ]
    #     print precision(result, testLabel), k
    classifyKdTree([2,2.5], trainSet, 1)

if __name__ == '__main__':
    # starttime = datetime.datetime.now()
    starttime = time.clock()
    main()
    # endtime = datetime.datetime.now() 
    endtime = time.clock()
    print 'Finished in %s s' %(endtime - starttime)
