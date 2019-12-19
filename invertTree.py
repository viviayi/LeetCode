# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:31:48 2019

@author: 11104510

左右翻转一颗二叉树
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        try:
            newTree = TreeNode(root.val)
        
            if root.right != None:
                newRight = Solution.invertTree(self,root.right)
                newTree.left = newRight
        
        
            if root.left != None:
                newLeft = Solution.invertTree(self,root.left)
                newTree.right = newLeft
        
            return newTree
        
        except:
            return root