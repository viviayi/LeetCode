# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:23:29 2019

@author: 11104510

python实现单向链表
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def get_data(self):
        return self.val
    
    def set_next(self, node):
        self.next = node
    
class SingleLinkedLists:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node
    
    def find(self, data):
        curr_node = self.head
        while curr_node.next is not None and curr_node.val != data:
            curr_node = curr_node.next
        return curr_node
        
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
    
    def print(self):
        output = []
        curr_node = self.head
        while curr_node.next is not None:
            output.append(curr_node.val)
            curr_node = curr_node.next
        output.append(curr_node.val)
        print(output)
        
if __name__ == '__main__':
    input_list = [1,3,5,4]
    input_delete_data = 5
    sll = SingleLinkedLists()
    for data in input_list:
        sll.append(data)
    sll.print()
    delete_node = sll.find(input_delete_data)
    sll.deleteNode(delete_node)
    sll.print()    