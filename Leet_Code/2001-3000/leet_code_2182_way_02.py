import time
from collections import Counter


class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        freq = Counter(s)
        chars = sorted(freq.keys(), reverse=True)
        result = ''


        while chars :
            current_char = chars[0]

            amount = min(freq[current_char], repeatLimit)
            result += current_char * amount

            freq[current_char] -= amount

            if freq[current_char] == 0:
                chars.pop(0)
            else :
                if len(chars) > 1:
                    result += chars[1]
                    freq[chars[1]] -= 1

                    if freq[chars[1]] == 0:
                        chars.pop(1)
                else:
                    break

        return result



print(Solution().repeatLimitedString("aababab", 2))
print(Solution().repeatLimitedString("cczazcc", 3))
print(Solution().repeatLimitedString("robnsdvpuxbapuqgopqvxdrchivlifeepy", 2))

