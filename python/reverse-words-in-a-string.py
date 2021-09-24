import re


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(
            list(
                map(
                    lambda word: "".join(reversed([char for char in word])),
                    re.split(r"\s", s),
                )
            )
        )
