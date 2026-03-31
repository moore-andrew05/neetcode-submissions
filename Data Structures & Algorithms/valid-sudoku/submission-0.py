class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes: list[dict[str, int]] = [defaultdict(int) for _ in range(9)]
        rows: list[dict[str, int]] = [defaultdict(int) for _ in range(9)]
        cols: list[dict[str, int]] = [defaultdict(int) for _ in range(9)]
        
        def scale_coords(coords: tuple[int, int]):
            return (coords[0] // 3, coords[1] // 3)

        def transform_coords(coords: tuple[int, int]):
            return (coords[0] * 3) + coords[1]

        for y, row in enumerate(board):
            for x, val in enumerate(row):
                rows[y][val] += 1
                cols[x][val] += 1
                boxes[transform_coords(scale_coords((y, x)))][val] += 1
        
        [boxes[i].pop('.') for i in range(9)]
        [rows[i].pop('.') for i in range(9)]
        [cols[i].pop('.') for i in range(9)]

        for i in range(9):
            for count in list(boxes[i].values()) + list(rows[i].values()) + list(cols[i].values()):
                if count > 1:
                    return False

        return True
            
