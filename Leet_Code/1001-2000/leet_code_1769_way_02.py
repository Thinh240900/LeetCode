class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        res = [0] * n
        right = 0
        left =0
        for i in range(1, n):
            if boxes[i] == '1':
                res[0] += i
                right += 1

        if boxes[0] == '1':
            left += 1

        for i in range(1, n):

            res[i] += res[i-1] - right + left
            if boxes[i] == '1':
                left += 1
                right -= 1

        return res


print(Solution().minOperations("110")) # 1 1 3
print(Solution().minOperations("001011")) # 11 8 5 4 3 4