class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = [0] * (len(nums) - k + 1)
        for i in range(len(nums) - k + 1):
            arr[i] = sum(nums[i:i+k])
        print(arr)
        dp = [0] * (len(arr) + 1)
        def find_solution(index, count, sum):

            if index >= len(arr) :
                return -1
            if count == 3:
                return sum
            # print('index', index,arr[index])
            # print('count', count)
            i =0
            result = 0
            while result  != -1:

                result = find_solution(index + k +i,count + 1, sum+arr[index] )
                # if result!= -1:
                #     print('result', result)
                i +=1
        for i in range(len(arr) -  (k* 2 )):
            print('start')
            find_solution(i, 0, arr[i])
        return 'asd'
print(Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))
# print(Solution().maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 2))