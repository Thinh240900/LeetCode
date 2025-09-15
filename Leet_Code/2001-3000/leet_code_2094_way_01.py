from collections import Counter


class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        counter = Counter(digits)
        ans = []
        for i in range(1,10):
            if counter[i] > 0 :
                counter[i] -= 1
                for j in range(10):
                    if counter[j] > 0:
                        counter[j] -= 1

                        for k in [0,2,4,6,8]:
                            if counter[k]:
                                ans.append(100*i + 10*j + k)
                        counter[j] +=1
                counter[i] +=1
        return ans



print(Solution().findEvenNumbers(digits = [2,1,3,0]))
print(Solution().findEvenNumbers(digits = [2,2,8,8,2]))
print(Solution().findEvenNumbers(digits = [3,7,5]))