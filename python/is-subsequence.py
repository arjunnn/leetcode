class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        if len(s) > len(t):
            return False
        j = 0
        s = list(s)
        t = list(t)
        for i in range(len(t) - 1):
            if t[i] == s[j]:
                i += 1
                j = min(j + 1, len(s))
                if j == len(s):
                    return True
            else:
                t[i] = None
                i += 1
        s = "".join(s)
        t = "".join([char for char in t if char])
        return s == t


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        found = 0
        for s_char in s:
            if s_char not in t:
                break
            for j in range(i, len(t)):
                t_char = t[j]
                if t_char == s_char:
                    found += 1
                    i = j + 1
                    break
            if j == len(t) - 1:
                break
        return found == len(s)
