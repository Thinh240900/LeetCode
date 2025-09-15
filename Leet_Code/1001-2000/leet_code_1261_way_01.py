# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements(object):
    root = None
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        arr = ass_value(root, 0, [])

        print(root.val)
        print(root.left)
        print(root.right.val)
        print(root.right.left.val)
        print(root.right.left.left.val)
        print (arr)
        self.root = arr

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.root

#
#
# ass_value(root, 0)
def ass_value(root, value, arr ):
    if not root:
        return arr
    root.val = value
    arr.append(root.val)
    arr = ass_value(root.left, value * 2 + 1, arr)
    arr = ass_value(root.right, value * 2 + 2, arr)
    return arr

# print(FindElements(TreeNode(-1, None, TreeNode(-1, None, None))))
print(FindElements(TreeNode(-1, None, TreeNode( -1, TreeNode( -1,  TreeNode( -1,  None,  None),  None),  None))).find(5))

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

