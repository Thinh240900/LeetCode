from collections import defaultdict, deque


class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        know, share = deque([(1, 1)]), deque([])
        know_cnt, share_cnt = 1, 0
        for i in range(2, n + 1):
            if know and know[0][0] == i - delay:
                know_cnt -= know[0][1]
                share_cnt += know[0][1]
                share.append(know[0])
                know.popleft()
            if share and share[0][0] == i - forget:
                share_cnt -= share[0][1]
                share.popleft()
            if share:
                know_cnt += share_cnt
                know.append((i, share_cnt))
        return (know_cnt + share_cnt) % (10 ** 9 + 7)




print(Solution().peopleAwareOfSecret( n = 6, delay = 1, forget = 2)) # 2
print(Solution().peopleAwareOfSecret( n = 6, delay = 2, forget = 4)) # 5
print(Solution().peopleAwareOfSecret(n = 4, delay = 1, forget = 3)) # 6