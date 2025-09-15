class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_nums = max(nums)
        left = 0
        n = len(nums)
        count_max = 0
        count = 0
        for i in range(n):
            if nums[i] == max_nums:
                count_max += 1
            while count_max >=k:
                count += n - i
                if nums[left] == max_nums:
                    count_max -= 1
                left += 1
        return count


print(Solution().countSubarrays([1,3,2,3,3], 2))
print(Solution().countSubarrays([1,4,2,1], 3))