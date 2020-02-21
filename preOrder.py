"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        outList = []
        if not root:
            pass
        outList.append(root.val)
        for child in root.children:
            outList += Solution.postorder(self,child)
        return outList
