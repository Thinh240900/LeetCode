from collections import defaultdict, Counter


class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums[0]
        count = 0
        x_count = 0
        n = len(nums)

        for num in nums:
            if num == x:
                count += 1
            else:
                count -= 1
            if count == 0:
                x = num
                count = 1

        # Count frequency of majority element
        for num in nums:
            if num == x:
                x_count += 1

        # Check if valid split is possible
        count = 0
        for index in range(n):
            if nums[index] == x:
                count += 1
            remaining_count = x_count - count
            if count * 2 > index + 1 and remaining_count * 2 > n - index - 1:
                return index

        return -1

print(Solution().minimumIndex([1,2,2,2])) # 2
print(Solution().minimumIndex([2,1,3,1,1,1,7,1,2,1])) # 4
print(Solution().minimumIndex([3,3,3,3,7,2,2])) # -1


