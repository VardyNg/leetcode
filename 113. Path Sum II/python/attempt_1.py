from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        # handle base case
        if root is None:
            return result

        def find_path_sum(node: TreeNode, paths, run_sum):
            # if reaches leaf, check path run_sum value
            if node is None:
                return

            # clone paths by value
            temp_path = paths[:]

            temp_path.append(node.val)
            run_sum += node.val
            if node.left is None and node.right is None:

                if run_sum == targetSum:
                    result.append(temp_path)

            return find_path_sum(node=node.left, paths=temp_path, run_sum=run_sum) or find_path_sum(node=node.right, paths=temp_path, run_sum=run_sum)

        find_path_sum(node=root, paths=[], run_sum=0)

        return result
            