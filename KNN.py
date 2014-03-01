import math
import numpy as np
import os
import sys

def dieWithUsage():
    print u'''
|***********************How to use Neual Networds******************************|
|  Example: python KNN.py [Flags] <trainSet> <testSet>  [ni] [nh] [no]         |
|******************************************************************************|
|  Flags:                                                                      |
|  -help        Display how to use the script                                  |
|------------------------------------------------------------------------------|
|  Parameters:                                                                 |
|  trainPath    Train data path                                                |
|  testPath     Test data path                                                 |
|  ni           Number of input nodes  (default = 2)                           |
|  nh           Number of hidden nodes (default = 2)                           |
|  no           Number of output nodes (default = 1)                           |
|------------------------------------------------------------------------------|
'''
    sys.exit(0)

def getParams():
    
    if len(sys.argv) < 3:
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
    trainSet = sys.argv[1]
    # print trainSet
    testSet = sys.argv[2]
    # print testSet
    if not os.path.exists(trainSet):
        print 'Train set: %s not found!!' %trainSet
    if not os.path.exists(testSet):
        print 'Test set: %s not found!!' %testSet

def readFile(trainSet, testSet):
    pass 

def main():
    getParams()

if __name__ == '__main__':
    main() 
