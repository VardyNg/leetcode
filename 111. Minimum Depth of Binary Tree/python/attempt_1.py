from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # handle base case
        if root is None:
            return 0

        # initialise minHeight
        # set as the maximum possible height of the tree
        # i.e. all 10^5 nodes in the tree are single children (except the root) => form a tree with height=10^5
        min_height = pow(10, 5)

        def find_min(height: int, node: TreeNode):

            nonlocal min_height
            if node is None:
                return

            # if node has no child, it's a leaf and can determine the height of the path (from root to leaf)
            if node.left is None and node.right is None:
                if height < min_height:
                    min_height = height
                return

            return find_min(height=height+1, node=node.left) or find_min(height=height+1, node=node.right)

        find_min(height=1, node=root)

        return min_height
