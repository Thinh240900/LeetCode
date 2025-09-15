class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = 0
        num_0_in_1 = 0
        sum2 = 0
        num_0_in_2 = 0

        for num in nums1:
            if num == 0 :
                num_0_in_1 += 1
            else:
                sum1 += num

        for num in nums2:
            if num == 0 :
                num_0_in_2 += 1
            else:
                sum2 += num

        if (num_0_in_1 == 0 and sum1 < sum2 + num_0_in_2) or (num_0_in_2 == 0 and sum2 < sum1 + num_0_in_1):
            return -1

        return max(sum1 + num_0_in_1, sum2 + num_0_in_2)

print(Solution().minSum(nums1 = [8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0], nums2 = [29,1,6,0,10,24,27,17,14,13,2,19,2,11])) # -1
print(Solution().minSum(nums1 = [2,0,2,0], nums2 = [1,4])) # -1

print(Solution().minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0])) # 12
