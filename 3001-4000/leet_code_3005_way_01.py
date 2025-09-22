class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counter = {}
        count_max = 0
        max_value = 0
        for num in nums:
            if counter.get(num):
                counter[num] += 1
                if max_value < counter[num]:
                    max_value = counter[num]
                    count_max = 1
                elif max_value == counter[num]:
                    count_max += 1
            else:
                counter[num] = 1
                if max_value < 1:
                    max_value = 1
                    count_max = 1
                elif max_value == 1:
                    count_max += 1
        return count_max * max_value






print(Solution().maxFrequencyElements([1,2,2,3,1,4])) # 4
print(Solution().maxFrequencyElements([1,2,3,4,5])) # 5
