class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[a-z0-9]+', re.IGNORECASE)
        matched = pattern.findall(s)
        s = ''.join(matched).lower()
        print(s)
        if len(s) == 1:
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True