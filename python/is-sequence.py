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
