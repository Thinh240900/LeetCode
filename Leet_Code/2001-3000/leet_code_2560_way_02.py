class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def checkRob(mid):
            house_rob = 0
            flag = False
            for num in nums:
                if flag:
                    flag = False
                elif num <= mid:
                    flag = True
                    house_rob += 1
            return house_rob >= k


        min_cap = 1
        max_cap = max(nums)
        while min_cap < max_cap:
            mid = (min_cap + max_cap) // 2
            if checkRob(mid):
                max_cap = mid
            else :
                min_cap = mid + 1
        return min_cap




print(Solution().minCapability([3,2,5,2,3,5,9], 3))
print(Solution().minCapability([2,3,5,9], 2))
print(Solution().minCapability([2,7,9,3,1], 2))