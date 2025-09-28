class Solution(object):
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(0, len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0

print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode", "warrier"], ["wrr","e"]))