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
        
"""
迭代法，每个节点依次遍历，需要先进先出，所以压栈需要逆向
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
        stack = [root,]
        while stack:
            _root = stack.pop()
            outList.append(_root.val)
            stack.extend(_root.children[::-1])
        return outList
