# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def preorderTraverse(self, root):
    if root is None:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.ledt)
    return res

def preorderTraverse0(root, result):
    if not root:
        return
    result.append(root.val)
    preorderTraverse0(root.left, result)
    preorderTraverse0(root.right, result)