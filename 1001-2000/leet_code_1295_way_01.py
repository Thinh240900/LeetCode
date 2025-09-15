class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        def count_digit(num):
            count = 1
            num = num // 10
            while num > 0:
                count +=1
                num = num // 10
            return count
        for i in range(n):
            if count_digit(nums[i]) % 2 == 0:
                ans +=1
        return ans

print(Solution().findNumbers([12,345,2,6,7896]))
print(Solution().findNumbers([555,901,482,1771]))