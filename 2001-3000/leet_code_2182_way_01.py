class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        char_count = {}
        for i in s:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1

        arr =[]
        arr_count = []
        for char in sorted(char_count.keys(), reverse=True):
            arr.append(char)
            arr_count.append(char_count[char])

        result = ''
        i = 0
        j = 0
        repeat_count =0
        while i < len(arr) and j < len(arr):
            if repeat_count == repeatLimit:
                if j != i and arr_count[j] > 0:
                    result += arr[j]
                    arr_count[j] -= 1
                    repeat_count = 0
                else:
                    j +=1
            else :
                if arr_count[i] > 0 :
                    result += arr[i]
                    repeat_count += 1
                    arr_count[i] -=1
                if arr_count[i] == 0:
                    i += 1
                    repeat_count = 0



        return result



print(Solution().repeatLimitedString("aababab", 2))
print(Solution().repeatLimitedString("cczazcc", 3))
print(Solution().repeatLimitedString("robnsdvpuxbapuqgopqvxdrchivlifeepy", 2))

