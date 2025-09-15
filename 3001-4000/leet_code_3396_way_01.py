

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        length_nums = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in temp:
                temp.append(nums[i])
                length_nums -= 1
            else:
                break

        result = 0
        while length_nums > 0:
            result += 1
            length_nums -= 3
        return result


print(Solution().minimumOperations([4,5,6,4,4])) # 2
print(Solution().minimumOperations([1,2,3,4,2,3,3,5,7])) # 2
print(Solution().minimumOperations([4,5,6,4,4])) # 2
print(Solution().minimumOperations([6,7,8,9])) # 0