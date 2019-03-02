# -*- coding: utf-8 -*-

#输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任
#意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，
#否则判题程序会直接返回空）
class RandomListNode:
    def __init__(self,x):
        self.label=x
        self.next=None
        self.random=None

#递归思想：把大问题转化若干子问题
class Solution:
    def Clone(self,pHead):
        if not pHead:
            return
        newnode=RandomListNode(pHead.label)
        newnode.random=pHead.random
        newnode.next=self.Clone(pHead.next)
        return newnode

#先遍历链表，把next的节点都复制好，然后再查看每个节点的random指向哪里了，就让新链表的
#random也指向哪里

class Solution0:
    def Clone(self,pHead):
        if not pHead:
            return None
        p=RandomListNode(pHead.label)
        #p链表的两个引用
        next_p=p
        random_p=p
        #pHead链表的引用
        random_pHead=pHead
        #遍历pHead链表，来修改next_p链表指向的值
        while pHead.next:
            next_p.next=RandomListNode(pHead.next.label)
            pHead=pHead.next
            next_p=next_p.next    
        #遍历random_pHead链表，用它的值修改random_p链表
        while random_pHead.next:
            if random_pHead.random:
                random_p.random=RandomListNode(random_pHead.random.label)
            random_pHead.next=random_pHead.next
            random_p=random_p.next
        return p

#python copy包中的深度拷贝
#copy:拷贝父对象，不会拷贝对象的内部的子对象
#deepcopy:完全拷贝了父对象及其子对象

class Solution1:
    def Clone(self,pHead):
        from copy import deepcopy
        return deepcopy(pHead)