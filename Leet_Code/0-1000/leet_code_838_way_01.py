class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        ans = dominoes
        i = 0

        def move_2_side(start, end):
            start_str = ""
            end_str = ""
            while start < end:
                start_str += "R"
                end_str += "L"
                start += 1
                end -= 1
            if start == end :
                return start_str + "." + end_str
            return start_str + end_str
        while i < n:
            note = i
            if dominoes[i] == 'L':
                i+=1
            elif dominoes[i] == 'R':
                i += 1
                if i >= n:
                    break
                while dominoes[i] == '.':
                    i += 1
                    if i >= n:
                        ans = ans[:note] + ('R' * (i - note)) + ans[i:]
                        i-=1
                        break
                    if dominoes[i] == 'R':
                        ans = ans[:note] + ('R' * (i - note)) + ans[i:]
                    if dominoes[i] == 'L':
                        ans = ans[:note] + move_2_side(note, i) + ans[i+1:]
                        i+=1
                        break
            if i >= n :
                break
            note = i

            while dominoes[i] == '.':
                i += 1
                if i >= n:
                    break
                if dominoes[i] == 'R':
                    break
                if dominoes[i] == 'L':
                    ans = ans[:note] + ('L' * (i - note)) + ans[i:]
                    i += 1
                    break
        return ans



print(Solution().pushDominoes("...RL....R.L.L........RR......L....R.L.....R.L..RL....R....R......R.......................LR.R..L.R."))
print(Solution().pushDominoes(".L"))
print(Solution().pushDominoes("RR.L"))
print(Solution().pushDominoes(".L.R...LR..L.."))
