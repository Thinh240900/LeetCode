from collections import defaultdict


class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        result = 1
        current = [0 for _ in range(n + 1)]
        current[delay+1:forget+1] = (a+1 for a in current[delay+1:forget+1])

        forget_arr = defaultdict(int)
        forget_arr[forget+1] = 1
        for i in range(2, n + 1):
            if forget_arr[i] > 0 :
                new_people = current[i]
                current[i+delay:i+forget] = (a + new_people for a in current[i+delay:i+forget])
                forget_arr[i+forget] = forget_arr[i+forget] + new_people
                result = (result + new_people - forget_arr[i]) % MOD
            else:
                new_people = current[i]
                forget_arr[i+forget] = forget_arr[i+forget] + new_people
                current[i+delay:i+forget] = (a + new_people for a in current[i+delay:i+forget])
                result = (result + new_people) % MOD


        return result % MOD




print(Solution().peopleAwareOfSecret( n = 6, delay = 1, forget = 2)) # 2
print(Solution().peopleAwareOfSecret( n = 6, delay = 2, forget = 4)) # 5
print(Solution().peopleAwareOfSecret(n = 4, delay = 1, forget = 3)) # 6