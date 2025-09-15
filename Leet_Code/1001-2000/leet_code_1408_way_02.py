class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sample = ' '.join(words)
        return [w for w in words if sample.count(w) > 1]


print(Solution().stringMatching(["mass","as","hero","superhero"]))
print(Solution().stringMatching(["leetcode","et","code"]))
print(Solution().stringMatching(["blue","green","bu"]))
print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))