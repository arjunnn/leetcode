class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        max_length = 0
        for char in s:
            if char in substring:
                if len(substring) > max_length:
                    max_length = len(substring)
                index = substring.index(char)
                substring = substring[index + 1 :]
                substring.append(char)
            else:
                substring.append(char)
        return len(substring) if len(substring) > max_length else max_length
