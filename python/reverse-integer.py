class Solution:
    def reverse(self, x: int) -> int:
        max_value = (2 ** 31) - 1
        min_value = -(2 ** 31)
        y = 0
        signed = x < 0
        x = abs(x)
        while x != 0:
            digit = x % 10
            y = (y * 10) + digit
            x = int(x / 10)
        if signed:
            y *= -1
        if y < 0 and y <= min_value:
            return 0
        elif y > max_value:
            return 0
        return y
