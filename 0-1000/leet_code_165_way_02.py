class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr_1 = version1.split('.')
        arr_2 = version2.split('.')
        for a,b in zip(arr_1, arr_2):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1

        n = len(arr_1)
        m = len(arr_2)
        if n > m:
            return 1 if any(int(a) > 0 for a in arr_1[m:]) else 0
        if m > n:
            return -1 if any(int(a) > 0 for a in arr_2[n:]) else 0
        return 0

print(Solution().compareVersion('1.0', '1.0.0.0'))
print(Solution().compareVersion('1.2', '1.10'))
print(Solution().compareVersion('1.01', '1.001'))

