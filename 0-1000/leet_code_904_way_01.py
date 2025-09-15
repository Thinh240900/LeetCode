from collections import defaultdict


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        answer = 0
        start = end = 0
        basket = defaultdict(int)
        for end in range(len(fruits)):
            basket[fruits[end]] += 1

            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            answer = max(answer, end - start + 1)
        return answer

print(Solution().totalFruit([0,1,2,2])) # 3
print(Solution().totalFruit([1,2,1])) # 3
print(Solution().totalFruit([1,2,3,2,2])) # 4