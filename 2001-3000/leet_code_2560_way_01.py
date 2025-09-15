class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_cap, max_cap = 1, max(nums)
        num_houses = len(nums)

        while min_cap < max_cap:
            mid = (min_cap + max_cap) // 2
            house_rob = 0

            index = 0
            while index < num_houses:
                if nums[index] <= mid:
                    house_rob += 1
                    index += 2
                else:
                     index += 1

            if house_rob >= k :
                max_cap = mid
            else :
                min_cap = mid + 1
        return min_cap




print(Solution().minCapability([3,2,5,2,3,5,9], 3))
print(Solution().minCapability([2,3,5,9], 2))
print(Solution().minCapability([2,7,9,3,1], 2))