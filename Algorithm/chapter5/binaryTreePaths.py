# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class BinaryTreePaths:
    def binaryTreePaths(self, root):
        if root is None:
            return []
        result = []
        self.dfs(root, [str(root.val)], result)
        return result
    
    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()
            
    def binaryTreePaths1(self, root):
        if root is None:
            return []
        result = []
        self.dfs1(root, [], result)
        return result
    
    def dfs1(self, root, path, result):
        path.append(str(root.val))
        if root.left is None and root.right is None:
            result.append('->'.join(path))
            path.pop()
            return
        if root.left:
            self.dfs1(root.left, path, result)
        if root.right:
            self.dfs1(root.right, path, result)
        path.pop()
        
    def binaryTreePaths2(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        paths = []
        for path in self.binaryTreePaths2(root.left):
            paths.append(str(root.val) + '->' + path)
        for path in self.binaryTreePaths2(root.right):
            paths.append(str(root.val) + '->' + path)
        return paths