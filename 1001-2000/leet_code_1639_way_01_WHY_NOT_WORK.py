import itertools


class Solution(object):
    def __init__(self):
        self.result = 0

    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        arr = [[0] * 26 for _ in range(len(words[0]))]
        for word in words:
            for i, char in enumerate(word):
                arr[i][ord(char) - 97] += 1
        combos = itertools.combinations(range(len(words[0])), len(target))
        for combo in combos:
            temp=1
            for index in combo:
                if arr[index][ord(target[combo.index(index)]) - 97] != 0:
                    temp *= arr[index][ord(target[combo.index(index)]) - 97]
                else:
                    temp =0
                    break
            self.result += temp
        return self.result

print(Solution().numWays(["acca","bbbb","caca"], "aba"))
print(Solution().numWays(["abba","baab"], "bab"))
print(Solution().numWays(["cbabddddbc","addbaacbbd","cccbacdccd","cdcaccacac","dddbacabbd","bdbdadbccb","ddadbacddd","bbccdddadd","dcabaccbbd","ddddcddadc","bdcaaaabdd","adacdcdcdd","cbaaadbdbb","bccbabcbab","accbdccadd","dcccaaddbc","cccccacabd","acacdbcbbc","dbbdbaccca","bdbddbddda","daabadbacb","baccdbaada","ccbabaabcb","dcaabccbbb","bcadddaacc","acddbbdccb","adbddbadab","dbbcdcbcdd","ddbabbadbb","bccbcbbbab","dabbbdbbcb","dacdabadbb","addcbbabab","bcbbccadda","abbcacadac","ccdadcaada","bcacdbccdb"], "bcbbcccc"))