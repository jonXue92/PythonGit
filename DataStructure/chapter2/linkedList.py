# -*- coding: utf-8 -*-
class Node(object):
    '''
    data:结点保存的数据
    next:保存下一个结点对象
    '''
    def __init__(self, data, pnext=None):
        self.data=data
        self.next=pnext
        
    def __repr__(self):
        '''
        用来定义Node的字符输出，print为输出data
        '''
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.length=0
        
    def isEmpty(self):
        return (self.length==0)
    
    def initial(self, lis):
        self.head=Node(lis[0])
        self.length=1
        p=self.head
        for i in lis[1:]:
            node=Node(i)
            p.next=node
            p=p.next
            self.length+=1
            
    def addHead(self, data):
        self.head=Node(data,self.head)
        self.length+=1
        
    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item=dataOrNode
        else:
            item=Node(dataOrNode)        
        if not self.head:
            self.head=item
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=item
        self.length+=1
    
    def delete(self, index):
        if self.isEmpty() or index<0 or index >= self.length:
            return        
        if index==0:
            self.head=self.head.next
            self.length-=1
            return        
        j=0
        node=self.head
        prev=self.head
        while node.next and j<index:
            prev=node
            node=node.next
            j+=1        
        if j==index:
            prev.next=node.next
            self.length-=1
            
    def removebydata(self, value):
        if self.isEmpty():
            return        
        if self.head.data==value:
            self.head=self.head.next
            self.length-=1
            return
        prev=self.head
        node=self.head.next
        while node.next:
            if node.data==value:
                prev.next=node.next
                self.length-=1
                return
            prev=prev.next
            node=node.next
        if node.data==value:
            prev.next=None
            self.length-=1
        else:
            return
        
    #在index的位置插入dataOrNode
    def insert(self, index, dataOrNode):
        if self.isEmpty() or index<0 or index>=self.length:
            return
        item=None
        if isinstance(dataOrNode, Node):
            item=dataOrNode
        else:
            item=Node(dataOrNode)
        if index==0:
            item.next=self.head
            self.head=item
            self.length+=1
            return
        j=0
        node=self.head
        prev=self.head
        while node.next and j<index:
            prev=node
            node=node.next
            j+=1
        if j==index:
            item.next=node
            prev.next=item
            self.length+=1
    
    def update(self,index,data):
        if self.isEmpty() or index<0 or index>=self.length:
            return
        j=0
        node=self.head
        while node.next and j<index:
            node=node.next
            j+=1
        if j==index:
            node.data=data
    
    def getItem(self,index):
        if self.isEmpty() or index<0 or index>=self.length:
            return
        j=0
        node=self.head
        while node.next and j<index:
            node=node.next
            j+=1
        return node.data
    
    def getIndex(self, data):
        j=0
        if self.isEmpty():
            return
        node=self.head
        while node:
            if node.data==data:
                return j
            node=node.next
            j+=1
        if j==self.length:
            return

    def getFirst(self):
        return self.head.data
    
    def getLast(self):
        node=self.head
        while node.next:
            node=node.next
        return node.data
    
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        prev=None
        while pHead:
            #先用temp保存pHead的下一个结点得的信息，
            #保证单链表不会因为失去pHead结点的next而就此断裂
            temp=pHead.next
            #保存完next,就可以让pHead的next指向prev
            pHead.next=prev
            #让prev，pHead依次向后移动一个结点，继续下一次的指针反转
            prev=pHead
            pHead=temp
        return prev
    
    def clear(self):
        self.head=None
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
    
    def __getitem__(self, ind):
        if self.isEmpty() or ind<0 or ind>=self.length:
            return
        return self.getItem(ind)
    
    def __setitem__(self, ind, val):
        if self.isEmpty() or ind<0 or ind>=self.length:
            return
        self.update(ind, val)
    
    def __len__(self):
        return self.length