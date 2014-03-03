import os
import sys
import numpy as np
from ipdb import set_trace

class Node(object):
    def __init__(self, data = None, left = None, right = None ):
        self.data = data
        self.left = left
        self.right = right

class KDNode(Node):
    def __init__(self, data = None, left = None, right = None, axis = None, sel_axis = None, dimensions = None):
        super(KDNode, self).__init__(data, left, right)
        self.axis = axis
        self.dimensions = dimensions

def createTree(dataList = None, dimensions = None, axis = 0, sel_axis = None):
    if not dataList and not dimensions:
        raise ValueError('List or dimensions must be provided')

    elif dataList:
        dimensions = dimensions or len(dataList[0])

    if not dataList:
        return KDNode(sel_axis = sel_axis, axis = axis, dimensions=dimensions)

    sel_axis = sel_axis or (lambda prev_axis: (prev_axis + 1) % dimensions) 
    dataList.sort(key = lambda point: point[axis]) 
    median = len(dataList) // 2
    loc = dataList[median]
    left = createTree(dataList[:median], dimensions, axis = sel_axis(axis))
    right = createTree(dataList[median + 1:], dimensions, axis = sel_axis(axis))
    return KDNode(loc, left, right, axis = axis, sel_axis = sel_axis)

def dist(nearest, target):
    print nearest, target
    nearMx = np.array(nearest)
    targetM = np.array(target)
    diff = (nearMx - targetM) ** 2
    dis = diff.sum(axis = 0)
    return dis ** 0.5

def isLeaf(kdNode):
    if kdNode.right == None and kdNode.left == None:
        return True
    else:
        return False

def searchTree(kdTree, target, k):
    # Create a stck to store search path
    stack = []
    nearestList = []
    distanceList = []
    # Store root node
    kdPoint = kdTree

    # Find the first leaf and generate search path
    while kdPoint.data != None:
        stack.append(kdPoint)
        axis = kdPoint.axis
        if target[axis] <= kdPoint.data[axis]:
            kdPoint = kdPoint.left
        else:
            kdPoint = kdPoint.right

    nearest = stack[-1].data
    distance = dist(nearest, target)
    nearestList.append(nearest)
    distanceList.append(distance)

    del(stack[-1])
    #print 'Finish search'

    while len(stack) > 0:
        backPoint = stack[-1]
        #print 'backPoint in traverse', backPoint.data
        del(stack[-1])
        if isLeaf(backPoint):
            if len(nearestList) <= k:
                nearest = backPoint.data
                distance = dist(backPoint.data, target)
                nearestList.append(nearest)
                distanceList.append(distance)
            else:
                if max(distanceList) > dist(backPoint.data, target):
                    idx = np.argmax(distanceList)
                    nearest = backPoint.data
                    distance = dist(backPoint.data, target)
                    nearestList[idx] = nearest
                    distanceList[idx] = distance
        else:
            axis = backPoint.axis
            if abs(backPoint.data[axis] - target[axis]) < distance:
                if len(nearestList) <= k:
                    nearest = backPoint.data
                    distance = dist(backPoint.data, target)
                    nearestList.append(nearest)
                    distanceList.append(distance)
                else:
                    if max(distanceList) > dist(backPoint.data, target):
                        idx = np.argmax(distanceList)
                        nearest = backPoint.data
                        distance = dist(backPoint.data, target)
                        nearestList[idx] = nearest
                        distanceList[idx] = distance
                if target[axis] <= backPoint.data[axis]:
                    kdPoint = backPoint.right
                else:
                    kdPoint = backPoint.left
            if len(stack) > 0 and kdPoint.data != None:
                stack.append(kdPoint)
                #print 'Append:', kdPoint.data
    return nearestList
