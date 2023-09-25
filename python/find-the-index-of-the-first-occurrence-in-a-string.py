import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pattern = re.compile(needle)
        match = pattern.search(haystack)
        if match:
            return match.span()[0]
        return -1
