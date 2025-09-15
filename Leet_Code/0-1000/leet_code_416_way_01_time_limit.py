class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total =sum(nums)
        if total % 2== 1 :
            return False
        result = int(total / 2)
        length_nums = len(nums)
        # nums.sort()
        def sumone(from_index, current):
            # print('current ', current)
            if current == result:
                return True
            for i in range(from_index, length_nums):
                if sumone(i+1, current + nums[i]):
                    return True


        for i in range(length_nums):
            # print('vong ngoai ' , i)
            if (sumone(i+1, nums[i])):
                return True
        return False

print(Solution().canPartition([14,9,8,4,3,2])) # True
print(Solution().canPartition([3,3,3,4,5])) # True
print(Solution().canPartition([1,5,12])) # False
print(Solution().canPartition([1,5,11,5])) # true
print(Solution().canPartition([1,2,3,5])) #Fasle