"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        outList = []
        if not root:
            return []
        if not root.children:
            return [root.val]
        outList.append(root.val)
        for child in root.children:
            outList.extend(Solution.preorder(self,child))
        return outList
        
