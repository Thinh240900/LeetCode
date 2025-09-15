class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] > k:
                return []
            else:
                ans.append([nums[i - 2], nums[i - 1], nums[i]])

        return ans


print(Solution().divideArray([1,3,4,8,7,9,3,5,1], 2)) # [[1,1,3],[3,4,5],[7,8,9]]
print(Solution().divideArray([2,4,2,2,5,2], 2)) # []
print(Solution().divideArray([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14)) # [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]