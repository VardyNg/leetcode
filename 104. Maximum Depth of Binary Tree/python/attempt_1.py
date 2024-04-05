from typing import Optional, List
from TreeNode import TreeNode

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # handle base case
        if root is None:
            return 0

        def find_max(height: int, node: TreeNode):
            if node is None:
                return 0

            print(node.val)
            if node.left is None and node.right is None:
                return height

            return max(
                find_max(height=height+1, node=node.left),
                find_max(height=height+1, node=node.right)
            )

        return find_max(height=1, node=root)
