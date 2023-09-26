class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = 0
        start = False
        for i in reversed(range(0, len(s))):
            if s[i] != " ":
                start = True
                j += 1
            elif start and s[i] == " ":
                break
        return j
