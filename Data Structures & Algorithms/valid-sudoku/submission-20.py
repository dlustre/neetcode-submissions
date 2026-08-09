class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # track a set for each row, each col, each subbox

        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        subboxSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                subbox = (i // 3) * 3 + (j // 3)

                num = board[i][j]

                if num == ".":
                    continue

                if num in rowSet[i]:
                    return False
                if num in colSet[j]:
                    return False
                if num in subboxSet[subbox]:
                    return False
                
                rowSet[i].add(num)
                colSet[j].add(num)
                subboxSet[subbox].add(num)
        
        return True