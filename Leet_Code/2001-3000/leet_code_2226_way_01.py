class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies) < k:
            return 0
        if sum(candies) == k:
            return 1

        temp = sorted(candies, reverse=True)
        max = temp[0]
        min = 1
        mid = round((max + min ) / 2)
        last_result = 0
        while max - min > -1:
            result = 0
            for i in temp:
                child = i // mid
                if child == 0:
                    break
                result += child
                if result >= k:
                    if last_result < mid:
                        last_result = mid
                    min = mid + 1
                    mid = round((max + min) / 2)
                    break

            if result < k:
                max = mid - 1
                mid = round((max + min) / 2)


        return int(last_result)


print(Solution().maximumCandies([9,10,1,2,10,9,9,10,2,2], 3)) # 9
print(Solution().maximumCandies([5,6,4,10,10,1,1,2,2,2], 9)) # 3
print(Solution().maximumCandies([4,7,5], 16)) # 1
print(Solution().maximumCandies([5,8,6], 3)) # 5
print(Solution().maximumCandies([2,5], 11)) # 0