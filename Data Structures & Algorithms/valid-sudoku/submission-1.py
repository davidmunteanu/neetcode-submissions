class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = defaultdict(set)

        for rowIdx, row in enumerate(board):
            for colIdx, plot in enumerate(row):

                if plot == '.':
                    continue

                if plot in visited[("row", rowIdx, 0)]:
                    return False
                if plot in visited[("col", colIdx, 0)]:
                    return False
                if plot in visited[("box", colIdx // 3, rowIdx // 3)]:
                    return False

                visited[("row", rowIdx, 0)].add(plot)
                visited[("col", colIdx, 0)].add(plot)
                visited[("box", colIdx // 3, rowIdx // 3)].add(plot)
        
        return True
        