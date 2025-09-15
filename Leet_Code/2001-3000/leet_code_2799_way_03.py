from collections import defaultdict


class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_nums = len(set(nums))
        left = 0
        right = 0
        n = len(nums)
        count = 0
        dict = defaultdict(int)
        current_distinct_nums = 0

        while right < n:
            dict[nums[right]] += 1
            if dict[nums[right]] == 1:
                current_distinct_nums += 1
            while current_distinct_nums == distinct_nums:
                count += n - right
                dict[nums[left]] -= 1
                if dict[nums[left]] == 0:
                    current_distinct_nums -= 1
                left += 1
            right +=1

        return count

print(Solution().countCompleteSubarrays([1454,1789,1454])) # 3
print(Solution().countCompleteSubarrays([1,3,1,2,2])) # 4
print(Solution().countCompleteSubarrays([5,5,5,5])) # 10
