from collections import defaultdict
from math import factorial


class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """





        dict = defaultdict(int)
        start  = 0
        end = 0
        total_pairs = 0
        result = 0
        length_nums = len(nums)
        while end <= length_nums:
            if total_pairs >= k:
                result += length_nums-end + 1
                dict[nums[start]] -= 1
                total_pairs -= dict[nums[start]]
                start += 1
            else:
                if end < length_nums:
                    total_pairs += dict[nums[end]]
                    dict[nums[end]] += 1
                end += 1

        return result


# print(Solution().countGood([1,1,1,1,1] , 10 ))
print(Solution().countGood([3,1,4,3,2,2,4], 2 )) # 4