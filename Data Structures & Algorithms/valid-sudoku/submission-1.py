class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        squares = [defaultdict(int) for _ in range(9)]

        checks = [rows, cols, squares]

        def get_square(x: int, y: int) -> int:
            return (y // 3) + (3 * (x // 3))

        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num == ".":
                    continue
                
                rows[x][num] += 1
                cols[y][num] += 1
                squares[get_square(x, y)][num] += 1

        for lst in checks:
            for check in lst:
                if check.values() and max(check.values()) > 1:
                    return False

        return True 
        
                