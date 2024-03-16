from typing import Optional, List
from TreeNode import TreeNode
import array as arr

class Solution:
    def tree_to_array(self, tree: TreeNode) -> arr:
        array = []
        queue = [tree]

        while len(queue) > 0:
            node = queue.pop(0)

            if node is None:
                array.append(None)

                continue
            array.append(node.val)

            queue.append(node.left)
            queue.append(node.right)


        return array

    def isSameArray(self, p: arr, q: arr) -> bool:
        if len(p) is not len(q):
            return False

        for i, val in enumerate(p):
            if val != q[i]:
                return False
        print("returning True")
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            # Handle both None scenarios
            return True

        # Generate sequence by Breadth-First Search for tree p and q
        p_array = self.tree_to_array(self, tree=p)
        q_array = self.tree_to_array(self, tree=q)

        print(f"p_array {p_array}")
        print(f"q_array {q_array}")
        # Determine same tree by whether sequence p and q are the same, 
        return self.isSameArray(self, p=p_array, q=q_array)