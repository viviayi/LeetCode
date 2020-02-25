"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#递归法
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
"""
迭代法关键点：利用栈，每次将根节点出栈时，都将子节点压入栈（这样能保证一条子线遍历到结束）
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        outList = []
        if not root:
            return []
        stack = [root,]
        while stack:
            _root = stack.pop()
            outList.append(_root.val)
            for child in _root.children:
                stack.append(child)
        return outList[::-1]
