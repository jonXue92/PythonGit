# -*- coding: utf-8 -*-

from preorderTraverse import TreeNode

def removeNode(root, value):
    dummy = TreeNode(0)
    dummy.left = root
    parent = findNode(dummy, root, value)
    node = None
    if parent.left and parent.left.val == value:
        node = parent.left
    elif parent.right and parent.right.val == value:
        node = parent.right
    else:
        return dummy.left
    deleteNode(parent, node)
    return dummy.left

def findNode(parent, node, value):
    if not node:
        return parent
    if node.val == value:
        return parent
    if value < node.val:
        return findNode(node, node.left, value)
    else:
        return findNode(node, node.right, value)
    
def deleteNode(parent, node):
    if not node.right:
        if parent.left == node:
            parent.left == node.left
        else:
            parent.right == node.left
    else:
        temp = node.right
        father = node
        while temp.left:
            father = temp
            temp = temp.left
        if father.left == temp:
            father.left = temp.right
        else:
            father.right = temp.right
        if parent.left == node:
            parent.left = temp
        else:
            parent.right = temp
        temp.left = node.left
        temp.right = node.right