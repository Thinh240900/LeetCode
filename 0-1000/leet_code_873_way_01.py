class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """


        n = len(arr)
        num_set = set(arr)
        max_len = 0
        for i in range(n):
            for j in range(i+1, n):
                prev = arr[j]
                curr = arr[i] + arr[j]
                curr_len =2
                while curr in num_set:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    max_len = max(curr_len, max_len)
        return max_len


print(Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(Solution().lenLongestFibSubseq([1,3,7,11,12,14,18]))

