class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        if all(x == 1 for x in nums):
            return n - 1

        if all(x == 0 for x in nums):
            return 0

        groups = []
        current = nums[0]
        count = 1
        for num in nums[1:]:
            if num == current:
                count += 1
            else:
                groups.append((current, count))
                current = num
                count = 1
        groups.append((current, count))

        max_streak = 0

        for i in range(1, len(groups) - 1):
            if groups[i][0] == 0 and groups[i][1] == 1:
                if groups[i-1][0] == 1 and groups[i+1][0] == 1:
                    merged = groups[i-1][1] + groups[i+1][1]
                    max_streak = max(max_streak, merged)

        max_single_block = max(length for val, length in groups if val == 1)

        return max(max_streak, max_single_block)

print(Solution().longestSubarray([1,1,0,1])) # 3
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1])) # 5
print(Solution().longestSubarray([1,1,1])) # 2
print(Solution().longestSubarray([1])) # 0
print(Solution().longestSubarray([0])) # 0
print(Solution().longestSubarray([0, 1, 0])) # 1
