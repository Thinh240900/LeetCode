from collections import Counter, defaultdict


class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        # count total num that % modulo == k
        count_x = 0

        # dictionary to store the count of count_x % modulo == k
        sum = defaultdict(int)
        # initial sum of count_x % modulo == k is 1, since count_x = 0
        sum[0] = 1
        result = 0
        for num in nums:
            # increasing count_x by 1 if num % modulo == k
            if num % modulo == k:
                count_x += 1

            # add result base on previous count_x that this count_x need to satisfy the second condition
            result += sum[(count_x - k) % modulo]
            ### Explain: pass num through nums, when come to a num it always have a count_x before it and it,
            # so it will need a prefix sum to meet second condition.

            # increasing the count of this count_x % modulo == k by 1
            sum[count_x % modulo] += 1

        return result


print(Solution().countInterestingSubarrays([3, 2, 4], 2, 1))  # 3
print(Solution().countInterestingSubarrays([3, 1, 9, 6], 3, 0))  # 2
