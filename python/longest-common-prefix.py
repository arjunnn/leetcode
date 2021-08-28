class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = list(set(strs))
        smallest = len(min(strs, key=len))
        strs = [word[:smallest] for word in strs]
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        length = len(prefix) or 1
        while True:
            if len(set([word[:length] for word in strs])) == 1:
                prefix = strs[0][:length]
                if len(prefix) == len(strs[0]):
                    return strs[0]
                if prefix:
                    length += 1
                    continue
            break
        return prefix