from pandocfilters import Space


class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_1 = 0
        count_2 = 0
        count_3 = 1
        current_3 = nums[0] % 2
        for num in nums:
            if num % 2 == 0:
                count_2 +=1
                if current_3 == 1:
                    count_3 += 1
                    current_3 = 0
            else:
                count_1 += 1
                if current_3 == 0:
                    count_3 += 1
                    current_3 = 1
        return max(count_1, count_2, count_3)

print(Solution().maximumLength([1,2,3,4])) # 4
print(Solution().maximumLength([1,2,1,1,2,1,2])) # 6
print(Solution().maximumLength([1,3])) # 2