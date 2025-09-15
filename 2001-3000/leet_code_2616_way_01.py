class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        def countValidPairs(threshold):
            count = 0
            index = 0
            while index < n - 1:
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        left, right = 0 , nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if countValidPairs(mid) >= p :
                right = mid
            else :
                left = mid + 1

        return left


print(Solution().minimizeMax(nums=[3,3,5,1,0,5,6,6], p=4))  # 1
print(Solution().minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))  # 1
print(Solution().minimizeMax(nums=[4, 2, 1, 2], p=1))  # 0
