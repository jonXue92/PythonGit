# -*- coding: utf-8 -*-

from preorderTraverse import TreeNode

def postorderTraversal(root, result):
    if not root:
        return
    postorderTraversal(root.left, result)
    postorderTraversal(root.right, result)
    result.append(root.val) # 注意访问根节点放到了最后