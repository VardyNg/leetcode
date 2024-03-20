from typing import Optional, List
from TreeNode import TreeNode
import array as arr

class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # handle if empty tree
        if root is None:
            return True

        def dfs(left, right):
            # if both left and right node are null -> symmetric
            if not left and not right:
                return True

            # if either left and right is None or their values does not match
            # the tree is not symmetric
            if not left or not right:
                return False

            if left.val != right.val:
                return False

            # otherwise, continue to search its child
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
