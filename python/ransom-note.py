class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        for r_char in ransomNote:
            print(r_char)
            if r_char in magazine:
                index = magazine.index(r_char)
                magazine = magazine[:index] + magazine[index + 1 : len(magazine)]
            else:
                return False
        return True
