# -*- coding: utf-8 -*-
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class SortedListToBST:
    def sortedListToBST(self, head):
        res = self.dfs(head)
        return res
    
    def dfs(self, head):
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = dummy
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
        temp = slow.next
        slow.next = None
        parent = TreeNode(temp.val)
        
        parent.left = self.dfs(head)
        parent.right = self.dfs(temp.next)
        
        return parent