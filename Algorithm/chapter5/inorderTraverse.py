# -*- coding: utf-8 -*-

from preorderTraverse import TreeNode

def inorderTraverse(self, root):
    if root is None:
        return []
    
    # 创建一个 dummy node, 右指针指向 root, 并放到 stack 里，此时 stack 的栈顶 dummy
    # 是 iterator 的当前位置
    dummy = TreeNode(-1)
    dummy.right = root
    stack = [dummy]
    
    res = []
    # 每次将 iterator 挪到下一个点，也就是调整 stack 使得栈顶到下一个点
    while stack:
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if stack:
            res.append(stack[-1].val)
    return res

def inorderTraverse0(root, result):
    if not root:
        return
    inorderTraverse0(root.left, result)
    result.append(root.val) # 注意访问根节点放到了遍历左子树的后面
    inorderTraverse0(root.right, result)