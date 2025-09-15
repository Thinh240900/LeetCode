from collections import defaultdict


class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        arr_index_violation = [-1]
        for i in range(len(nums)):
            if nums[i] < minK:
                arr_index_violation.append(i)
            if nums[i] > maxK:
                arr_index_violation.append(i)
        arr_index_violation.append(len(nums))

        def count_subarrays(left, right):
            dict = defaultdict(int)
            dict[minK] = 0
            dict[maxK] = 0
            count = 0
            left_index = left
            for i in range(left+1, right):
                if nums[i] == minK or nums[i] == maxK:
                    dict[nums[i]] += 1
                while dict[minK] > 0 and dict[maxK] > 0:
                    count += right - i
                    left_index += 1
                    dict[nums[left_index]] -= 1
            return count



        result = 0
        for i in range(len(arr_index_violation) - 1):
            result += count_subarrays(arr_index_violation[i], arr_index_violation[i + 1])  # (right - left) - 1
        return result

print(Solution().countSubarrays([1,2,1,3,5,2,7,5], 1, 5)) # 6
print(Solution().countSubarrays([1,3,5,2,7,5], 1, 5)) # 2
print(Solution().countSubarrays([1,1,1,1], 1, 1)) # 10