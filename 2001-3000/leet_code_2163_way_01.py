class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 3
        max = 0
        min = sum(nums)
        ans = min
        for i in range(n-1, len(nums)-n+1):
            print(i)
            print(sorted(nums[:i+1]))


print(Solution().minimumDifference([3,1,2])) # -1
print(Solution().minimumDifference([7,9,5,8,1,3])) # 1