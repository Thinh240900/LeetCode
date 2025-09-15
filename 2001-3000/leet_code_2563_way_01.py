from collections import deque


class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()

        def find_left(target, start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] >= target:
                    end = mid -1
                elif nums[mid] < target:
                    start = mid + 1
            return start

        def find_right(target, start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] <= target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
            return end

        result = 0
        for i in range(len(nums)-1):
            left = find_left(lower - nums[i], i + 1 , len(nums)-1)
            right = find_right(upper - nums[i], i + 1 , len(nums)-1)
            # result += right - left
            # print('nums[i]: ', nums[i])
            # print('left: ', left)
            # print('right: ', right)
            if right >= left:
                result += right - left + 1
            # print('result: ', result)

        return result



print(Solution().countFairPairs( [0,0,0,0,0,0], 0, 0)) # 15
print(Solution().countFairPairs( [1,7,9,2,5], 11, 11)) # 1
print(Solution().countFairPairs([0,1,7,4,4,5], 3,6)) # 6
