class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        stack = []
        for i in range(len(arr)):
            stack.append(arr[i])
            while stack and  stack[0] <= i:
                stack.pop(0)
            if not stack:
                count += 1

        return count


print(Solution().maxChunksToSorted([4, 3, 2, 1, 0])) # 1
print(Solution().maxChunksToSorted([1, 0, 2, 3, 4])) # 4
print(Solution().maxChunksToSorted([1, 0, 3, 2, 5, 4])) #  3
print(Solution().maxChunksToSorted([1, 5, 0, 2, 3, 4]))# 1
print(Solution().maxChunksToSorted([1, 2, 0, 3])) # 2
