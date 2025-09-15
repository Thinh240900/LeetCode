from collections import defaultdict
from math import factorial


class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        result =0
        dict1 = defaultdict(list)
        for i in range(n):
            dict1[nums[i]].append(i)
        for value in dict1.values():
            n = len(value)
            for i in range(n-1):
                for j in range(i+1, n):
                    if value[i] * value[j] % k == 0:
                        result +=1

        return (result)



print(Solution().countPairs([10,2,3,4,9,6,3,10,3,6,3,9,1], 4)) # 8
print(Solution().countPairs([3,1,2,2,2,1,3], 2)) # 4
print(Solution().countPairs([1,2,3,4], 1)) # 0