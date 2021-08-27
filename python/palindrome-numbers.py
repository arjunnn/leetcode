class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        return x == "".join([i for i in reversed([i for i in x])])
