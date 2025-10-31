from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_set = set()
        ans = []
        for num in nums:
            if num in count_set:
                ans.append(num)
            else:
                count_set.add(num)

        return ans


print(Solution().getSneakyNumbers([0,1,1,0])) # [1,0]
print(Solution().getSneakyNumbers([0,3,2,1,3,2])) # [3,2]
print(Solution().getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2])) # [4,5]