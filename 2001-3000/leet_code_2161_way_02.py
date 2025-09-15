

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result = []
        temp=[]
        for i in nums:
            if i < pivot:
                result.append(i)
            elif i > pivot:
                temp.append(i)

        return result + [pivot]*(len(nums) - len(result) - len(temp)) + temp

print(Solution().pivotArray([9,12,5,10,14,3,10], 10))
print(Solution().pivotArray([-3,4,3,2], 2))