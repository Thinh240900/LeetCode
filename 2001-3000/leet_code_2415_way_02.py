class TreeNode(object): 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def reverseOddLevels(self, root):
        # Helper function to recursively reverse odd levels
        def flip(left, right, is_odd):
            if not left or not right:
                return root

                # Reverse values at the current level if it's odd
            if is_odd:
                left.val, right.val = right.val, left.val

                # Recursively flip child levels
            flip(left.left, right.right, not is_odd)
            flip(left.right, right.left, not is_odd)

            return root

            # Start recursion from root, even level initially

        return flip(root.left, root.right, True)



arr = (Solution().reverseOddLevels(TreeNode(2,
                                           TreeNode(3, TreeNode(8, TreeNode(1), TreeNode(1)), TreeNode(13, TreeNode(1), TreeNode(1))), TreeNode(5, TreeNode(21, TreeNode(2), TreeNode(2)), TreeNode(34, TreeNode(2), TreeNode(2))))))

print(arr.val)
print(arr.left.val)
print(arr.right.val)