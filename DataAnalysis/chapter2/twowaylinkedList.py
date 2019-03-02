# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, data, pnext=None, pprev=None):
        self.data=data
        self.next=pnext
        self.prev=pprev
        
    def __repr__(self):
        return str(self.data)
    
class TwowayLinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def isEmpty(self):
        return (self.length==0)
    
    def add(self,dataOrNode):
        item=None
        if isinstance(dataOrNode,Node):
            item=dataOrNode
        else:
            item=Node(dataOrNode)
        if not self.head:
            self.head=item
            self.tail=item
            self.head.prev=None
            self.tail.next=None
            self.tail.prev=None
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=item
            self.tail=item
            self.tail.prev=node
            self.tail.next=None
        self.length+=1
    
    #在结点值为value的结点后面增加结点dataOrNode
    def insertbydata(self, value, dataOrNode):
        if self.isEmpty():
            return
        item=None
        if isinstance(dataOrNode,Node):
            item=dataOrNode
        else:
            item=Node(dataOrNode)
        node=self.head
        nex=node.next
        while node and node.data!=value:
            node=node.next
            nex=nex.next
        if node.next==None:
            node.next=item
            self.tail=item
            self.tail.prev=node
            self.tail.next=None
        else:
            item.prev=node
            item.next=node.next
            node.next=item
            nex.prev=item
        self.length+=1
    
    def deletebydata(self, value):
        if self.isEmpty():
            return
        if self.head.data==value:
            if self.length==1:
                self.head=None
                self.tail=None
            else:
                nex=self.head.next
                self.head=self.head.next
                nex.prev=None
            self.length-=1
        else:
            node=self.head.next
            while node and node.data!=value:
                node=node.next
            pre=node.prev
            if node:
                if node.next == None:
                    self.tail=pre
                    self.tail.next=None
                else:
                    nex=node.next
                    pre.next=node.next
                    nex.prev=pre
                self.length-=1
    
    def clear(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def __repr__(self):
        if self.isEmpty():
            return
        node=self.head
        nlist=''
        while node:
            nlist+=str(node.data)+' '
            node=node.next
        return nlist
    
    def reverse_repr(self):
        if self.isEmpty():
            return
        node=self.tail
        nlist=''
        while node:
            nlist+=str(node.data)+' '
            node=node.prev
        return nlist