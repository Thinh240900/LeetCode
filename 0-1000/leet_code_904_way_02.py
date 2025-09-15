from collections import defaultdict


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = {}
        left = 0
        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1
            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
        return right - left + 1

print(Solution().totalFruit([0,1,0,2,1])) # 3
print(Solution().totalFruit([1,2,1])) # 3
print(Solution().totalFruit([1,2,3,2,2])) # 4