class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i:min(i+k, len(s))].ljust(k, fill))
        return ans


print(Solution().divideString(s = "abcdefghi", k = 3, fill = "x")) # ["abc","def","ghi"]
print(Solution().divideString(s = "abcdefghij", k = 3, fill = "x")) # ["abc","def","ghi","jxx"]