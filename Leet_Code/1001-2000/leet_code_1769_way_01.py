class Solution(object):
    # def minOperations(self, boxes):
    #     """
    #     :type boxes: str
    #     :rtype: List[int]
    #     """
    #     n = len(boxes)
    #     res = [0] * n
    #     res[0] = int(boxes[0])
    #
    #     for i in range(1, n):
    #         res[i] = res[i - 1] + i * int(boxes[i]) - 1
    #
    #     for i in range(n - 2, -1, -1):
    #         res[i] += n - i - 1 - int(boxes[i])
    #
    #     return res
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        arr = [0] * n
        for i in range(n):
            if boxes[i] == '1':
                for j in range(n):
                    arr[j] += abs(i - j)
        return arr


print(Solution().minOperations("110"))
print(Solution().minOperations("001011"))