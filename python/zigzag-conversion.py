class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = []
        for i in range(numRows):
            rows.append([])
        string = [char for char in reversed(s)]
        fill_all = True
        for char in s:
            zigzag_pos = max([len(rows) - 2, 1 if numRows > 2 else 0])
            if fill_all:
                for row in rows:
                    try:
                        row.append(string.pop())
                    except: 
                        break
                fill_all = False if numRows > 2 else True
            else:
                zigzag = True
                try:
                    while zigzag:
                        for index, row in enumerate(rows):
                            if index != zigzag_pos:
                                continue
                            row.append(string.pop())
                            if zigzag_pos == (1 if numRows > 1 else 0):
                                zigzag = False
                            zigzag_pos = max([zigzag_pos - 1, 1 if numRows > 2 else 0])
                    fill_all = True
                except:
                    break
        return "".join(["".join(row) for row in rows])