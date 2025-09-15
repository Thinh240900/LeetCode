class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        index = 0
        while index < len(nums):
            if nums[index] == 0 :
                arr.append(0)
                index += 1
            else:
                count = 0
                while index < len(nums) and nums[index] == 1:
                    count += 1
                    index += 1
                arr.append(count)
        longest_subarray = max(arr) - 1 if len(arr) == 1 else max(arr)
        for i in range(len(arr)-2):
            if arr[i] + arr[i+2] > longest_subarray:
                longest_subarray = arr[i] + arr[i+2]

        return 0 if longest_subarray < 0 else longest_subarray

print(Solution().longestSubarray([1,1,0,1])) # 3
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1])) # 5
print(Solution().longestSubarray([1,1,1])) # 2
