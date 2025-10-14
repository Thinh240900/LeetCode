from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def check_increasing(nums: List[int]) -> bool:
            for i in range(len(nums) - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        for i in range(0, len(nums)-(k*2)+1):
            if check_increasing(nums[i:i+k]) and check_increasing(nums[i+k:i+2*k]):
                return True

        return False


print(Solution().hasIncreasingSubarrays(nums = [2,5], k = 1))
print(Solution().hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3))
print(Solution().hasIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7], k = 5))