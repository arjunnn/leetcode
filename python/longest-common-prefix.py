class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        common_prefix = ""
        length = len(common_prefix) or 1
        while True:
            if len(set([word[:length] for word in strs])) == 1:
                common_prefix = strs[0][:length]
                if len(common_prefix) == len(strs[0]):
                    return strs[0]
                if common_prefix:
                    length += 1
                    continue
            break
        return common_prefix
