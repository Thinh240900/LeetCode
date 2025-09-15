# Definition for a binary tree node.
from tkinter.constants import SOLID


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.arr = [val]
    def assignArr(self, current):
        if current.left:
            self.arr.append(current.left.val)
        if current.right:
            self.arr.append(current.right.val)
        if current.left:
            self.assignArr(current.left)
        if current.right:
            self.assignArr(current.right)


    def printArr(self):
        return self.arr
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        queue = []
        i=0
        result = ''
        while i< len(traversal) and  traversal[i].isnumeric():
                result += traversal[i]
                i+=1

        node = TreeNode(int(result))
        queue.append(node)
        while i < len(traversal):
            count = 1
            while i < len(traversal) and traversal[i] == '-':
                i+=1
                count += 1
            if count == len(queue)+1:
                result = ''
                while i < len(traversal) and  traversal[i].isnumeric():
                    result += traversal[i]
                    i += 1
                newNode = TreeNode(int(result))
                if not queue[-1].left:
                    queue[-1].left = newNode
                else :
                    queue[-1].right = newNode
                queue.append(newNode)
            elif count == len(queue):
                queue.pop()
                result = ''
                while i < len(traversal) and traversal[i].isnumeric():
                    result += traversal[i]
                    i += 1
                newNode = TreeNode(int(result))
                if not queue[-1].left:
                    queue[-1].left = newNode
                else:
                    queue[-1].right = newNode
                queue.append(newNode)
            elif count < len(queue):
                while count <= len(queue):
                    queue.pop()
                result = ''
                while i < len(traversal) and traversal[i].isnumeric():
                    result += traversal[i]
                    i += 1
                newNode = TreeNode(int(result))
                if not queue[-1].left:
                    queue[-1].left = newNode
                else:
                    queue[-1].right = newNode
                queue.append(newNode)

        node.assignArr(node)
        return node.printArr()

# print(Solution.recoverFromPreorder(Solution, "1-2--3--4-5--6--7"))
# print(Solution.recoverFromPreorder(Solution, "1-2--3--4-5--6--7"))
# print(Solution.recoverFromPreorder(Solution, "1-2--3---4-5--6---7"))
# print(Solution.recoverFromPreorder(Solution, "1-401--349---90--88"))
print(Solution.recoverFromPreorder(Solution, "1-401--349--90---88"))

# tn = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), None) , TreeNode(5, TreeNode(6, TreeNode(7))))
# tn.assignArr(tn)
# print(tn.printArr())
# tn = TreeNode(1, TreeNode(401, TreeNode(349, TreeNode(90)), TreeNode(88)))
# tn.assignArr(tn)
# print(tn.printArr())





# note: go depth each branch if have