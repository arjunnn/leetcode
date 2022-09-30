from collections import defaultdict, Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_char_map = defaultdict(lambda: [])
        t_char_map = defaultdict(lambda: [])
        for pos, char in enumerate(s):
            s_char_map[char].append(pos)
        for pos, char in enumerate(t):
            t_char_map[char].append(pos)
        s_positions = []
        for char in s:
            s_positions.append(s_char_map[char])
        t_positions = []
        for char in t:
            t_positions.append(t_char_map[char])
        for index, positions in enumerate(s_positions):
            if Counter(positions) != Counter(t_positions[index]):
                return False
        return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))