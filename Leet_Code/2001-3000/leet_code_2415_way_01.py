# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def oddArray(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()

            if node:
                if level % 2 == 0:
                    result.append(node.val)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        # while result:
        #     if result:
        #         print(result.pop(0).val)
        # for i in range(5):
        #     result.pop(0)
        # while result:
        #     if result:
        #         print(result.pop(0).val)
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()

            if node:
                if level % 2 == 0:
                    node.val = result.pop(0)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))


    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.oddArray(root)
        return root

arr = (Solution().reverseOddLevels(TreeNode(2,
                                           TreeNode(3, TreeNode(8, TreeNode(1), TreeNode(1)), TreeNode(13, TreeNode(1), TreeNode(1))), TreeNode(5, TreeNode(21, TreeNode(2), TreeNode(2)), TreeNode(34, TreeNode(2), TreeNode(2))))))

print(arr.val)
print(arr.left.val)
print(arr.right.val)