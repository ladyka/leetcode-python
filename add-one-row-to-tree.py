from typing import Optional
from tree_node import TreeNode


# 623. Add One Row to Tree
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

        Note that the root node is at depth 1.

        The adding rule is:

            Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
            cur's original left subtree should be the left subtree of the new left subtree root.
            cur's original right subtree should be the right subtree of the new right subtree root.
            If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
        """

        if depth == 1:
            return TreeNode(val=val, left=root)
        dive = 2
        row = [root]
        while depth > dive:
            # print(f"dive={dive} depth={depth}")
            current_row = []
            for node in row:
                if node.left is not None:
                    current_row.append(node.left)
                if node.right is not None:
                    current_row.append(node.right)
            dive += 1
            # print(current_row)
            row = current_row
        # print("=======================")
        for node in row:
            # print(node)
            node.left = TreeNode(val=val, left=node.left)
            node.right = TreeNode(val=val, right=node.right)

        return root


if __name__ == '__main__':
    s = Solution()
    print(s.addOneRow(TreeNode(val=10), val=4, depth=1))
    print(s.addOneRow(TreeNode(val=10), val=4, depth=2))
