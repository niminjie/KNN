from numpy import *
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
        if len(line.strip().split()) >= 3:
            trainLabel.append(float(line.strip().split()[2]))

    for line in open(testPath, 'r'):
        row = convertToDouble(line.strip().split()[0:2])
        testSet.append(row)
        if len(line.strip().split()) >= 3:
            testLabel.append(float(line.strip().split()[2]))

    if head == False:
         return trainSet[1:], testSet[1:], trainLabel[1:], testLabel[1:]
    else:
         return trainSet, testSet, trainLabel, testLabel

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

def main():
    getParams()
    readFile(trainPath, testPath)
    trainSet, testSet, trainLabel, testLabel = readFile(trainPath, testPath)
    print makeMatrix(trainSet, testSet)
    # print trainSet
    # print testSet
    # print testLabel

if __name__ == '__main__':
    main() 
