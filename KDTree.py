import sys
import os

class KDNode:
    pass

def createTree(kdNode, pointList, depth):
    if pointList == None:
        return None

    axis = depth % len(pointList[0])
    node.left = createTree()
