class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        left = 0
        right = 0
        total = 0
        n = len(nums)
        while left < n:
            if right < n and (total + nums[right]) * (right - left + 1) < k:
                total += nums[right]
                right += 1
            else:
                count += right - left
                total -= nums[left]  # subtract the leftmost element of the current subarray
                left += 1
        return count

print(Solution().countSubarrays([2,1,4,3,5], 10)) # 6
print(Solution().countSubarrays([1,1,1], 5)) # 5
