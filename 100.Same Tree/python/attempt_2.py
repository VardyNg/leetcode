from typing import Optional, List
from TreeNode import TreeNode
import array as arr

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use recursion to check every node in the tree
        # first check the substree structure
        # then check the node value

        # if the processing p and q (child) are none, it means the parent is leaf and p & q have same tree structure
        # early return True as no need to check value and has the same tree structure

        if p is None and q is None:
            return True

        # otherwise, if either p and q is None, return False as not the same tree structure
        if p is None or q is None:
            return False

        # check if p and q have the same tree structure
        # i.e. if p has left/right but q does not
        # if not, early return False as no need to chedk value
        if (p.left is None) is not (q.left is None):
            return False

        # same apply to the right node
        if (p.right is None) is not (q.right is None):
            return False

        # compare the value
        if p.val != q.val:
            return False

        # at this point, the p and q subtree are the same
        # call isSameTree again to check the child
        return self.isSameTree(self=Solution, p=p.left, q=q.left) and self.isSameTree(self=Solution, p=p.right, q=q.right)