from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [root.val]
        sums = []
        self.sumValues(root, stack, sums)
        return sum(sums)

    def sumLeaf(self, root, stack, sums):
        if root is not None:
            stack.append(root.val)
            self.sumValues(root, stack, sums)
            stack.pop()

    def sumValues(self, root: Optional[TreeNode], stack, sums):
        if (root.left is None) and (root.right is None):
            result = int(''.join(map(str, stack)))
            sums.append(result)
        self.sumLeaf(root.left, stack, sums)
        self.sumLeaf(root.right, stack, sums)


if __name__ == '__main__':
    s = Solution()
    print(s.sumNumbers(None))
    print(s.sumNumbers(TreeNode(val=10)))
    print(s.sumNumbers(TreeNode(val=10)))
