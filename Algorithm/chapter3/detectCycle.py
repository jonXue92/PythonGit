# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
class DetectCycle:
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None