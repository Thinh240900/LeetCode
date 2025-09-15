class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        i = 1
        while i < n :
            count = 0
            value = None
            temp = ''
            for char in result:
                if char != value:
                    if value:
                        temp += str(count) + value
                    count = 1
                    value = char
                else :
                    count +=1
            result = temp + str(count) + value
            i +=1
        return result



print(Solution().countAndSay(4))
print(Solution().countAndSay(1))
