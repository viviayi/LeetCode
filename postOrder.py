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
            return []
        if not root.children:
            return [root.val]
        for child in root.children:
            outList.extend(Solution.postorder(self,child))
        outList.append(root.val)
        return outList
