# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:18:28 2019

@author: 11104510

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        mergedNode = TreeNode(0)
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            mergedNode.val = t1.val + t2.val
            if t1.left is None:
                mergedNode.left = t2.left
            elif t2.left is None:
                mergedNode.left = t1.left
            else:
                mergedNode.left = Solution.mergeTrees(self, t1.left, t2.left)
        
            if t1.right is None:
                mergedNode.right = t2.right
            elif t2.right is None:
                mergedNode.right = t1.right
            else:
                mergedNode.right = Solution.mergeTrees(self, t1.right, t2.right)
            return mergedNode