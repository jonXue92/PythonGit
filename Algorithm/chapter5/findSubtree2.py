# -*- coding: utf-8 -*-

class FindSubtree2:
    average, node = 0, None
    def findSubtree2(self, root):
        self.helper(root)
        return self.node
    
    def helper(self, root):
        if root is None:
            return 0, 0
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        sum, size = left_sum + right_sum + root.val, left_size + right_size + 1
        if self.node is None or sum / size > self.average:
            self.node = root
            self.average = sum / size
        return sum, size