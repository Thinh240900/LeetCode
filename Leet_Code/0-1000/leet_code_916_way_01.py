class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        arr = []
        dict = [0]*26
        def count(word):
            temp = [0]*26
            for char in word:
                temp[ord(char)-ord('a')] += 1
            return temp

        for word in words2:
            for i,c in enumerate(count(word)):
                dict[i] = max(dict[i], c)

        for word in words1:
            if all(x >= y for x,y in zip(count(word), dict)):
                arr.append(word)



        return arr


print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode", "warrier"], ["wrr","e"]))