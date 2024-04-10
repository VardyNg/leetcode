from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        print("hasPathSum")
        # Handle base case
        if root is None:
            return False

        def find_path_sum(node: TreeNode, sum: int):
            print(f'find_path_sum: {sum}')
            if node is None:
                return False
            print("node is not None")
            # when reaches leaf, check the sum value

            sum = sum + node.val

            if node.left is None and node.right is None:
                if sum == targetSum:
                    return True
            print("node is not leaft")
            return find_path_sum(node=node.left, sum=sum) or find_path_sum(node=node.right, sum=sum)

        return find_path_sum(node=root, sum=0)
