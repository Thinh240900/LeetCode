

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result = []
        temp=[]
        equal= []
        for i in range(len(nums)):
            if nums[i] < pivot:
                result.append(nums[i])
            elif nums[i] > pivot:
                temp.append(nums[i])
            else:
                equal.append(nums[i])

        return result + equal + temp

print(Solution().pivotArray([9,12,5,10,14,3,10], 10))
print(Solution().pivotArray([-3,4,3,2], 2))