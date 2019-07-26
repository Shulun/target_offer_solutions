# -*- coding: utf-8 -*-

'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def getNext(self, pNode):
        if pNode == None:
            return None
        pNext = None
        # explore all the left nodes to find next
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left != None:
                pRight = pRight.left
            pNext = pRight
        # explore all the root nodes to find next
        elif pNode.next != None:
            pCurrent = pNode
            pParent = pCurrent.next
            while pParent != None and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pCurrent.next
            pNext = pParent
        return pNext


class Solution2:
    def getNext(self, pNode):
        if pNode == None:
            return None
        pNext = None
        # if input node has right subtree, the next node will be the 
        # the leftmost point of the right subtree
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode
        else:
            # if the current node has parent node and it is the parent
            # node's left node, then the next node will be its parent node
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            # if the current node has parent node and it is the parent
            # node's right node, iterate above and stops until the current
            # node is its parent node's left node, then the input node's 
            # next node will be the current node's parent node
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right:
                    pNode = pNode.next
                # if the current node still has a parent node when the
                # iteration is over, then the current node is its parent node's
                # left node. the input node's next node is the current node's
                # parent node. else if the current node does not have a parent
                # node at the end of iteration, the current node is at the right
                # subtree of the root node and there is no next node.
                # if pNode.next:
                #     pNext = pNode.next
                pNext = pNode.next
        return pNext