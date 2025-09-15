# Not solved completely
# Time limit exceeded

class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        if sum(nums) == 0:
            return 0
        k = 0

        for i in queries:
            k += 1
            for j in range(i[0], i[1]+1):
                nums[j] = 0 if nums[j] - i[2] < 0 else nums[j] - i[2]
            if sum(nums) == 0 :
                return k

        return -1

print(Solution().minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))
print(Solution().minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))