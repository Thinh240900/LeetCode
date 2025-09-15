class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        arr =[]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    arr.append(words[i])
                if words[j] in words[i]:
                    arr.append(words[j])
        return list(set(arr))
print(Solution().stringMatching(["mass","as","hero","superhero"]))
print(Solution().stringMatching(["leetcode","et","code"]))
print(Solution().stringMatching(["blue","green","bu"]))
print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))