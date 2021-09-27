import re


class Solution:
    def isValid(self, s: str) -> bool:
        # while True:
        #     s, n = re.subn(r'\(\)|\{\}|\[\]', '', s)
        #     if n == 0:
        #         break
        # return not s
        par_map = {p[1]: p[0] for p in "() {} []".split(" ")}
        values = par_map.values()
        opened = []
        i = 0
        while i < len(s):
            bracket = s[i]
            if bracket in values:
                opened.append(bracket)
            elif par_map[bracket] in opened:
                last_opened = opened.pop()
                if last_opened != par_map[bracket]:
                    return False
            else:
                return False
            i += 1
        return not opened
