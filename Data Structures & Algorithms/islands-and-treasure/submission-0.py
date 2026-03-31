class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def get_neighbors(y, x) -> List[tuple[int, int]]:
            DIRS = (
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0)
            )
            ret = []
            for dy, dx in DIRS:
                newy = y + dy
                newx = x + dx
                if newy >= 0 and newy < len(grid) and \
                    newx >= 0 and newx < len(grid[0]):
                    ret.append((newy, newx))
            return ret 
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != 0:
                    continue

                # coords + distance from chest
                q = deque([(y, x, 0)])
                while q:
                    y, x, dist = q.popleft()
                    if grid[y][x] < dist:
                        continue
                    for ny, nx in get_neighbors(y, x):
                        if grid[ny][nx] != -1:
                            q.append((ny, nx, dist + 1))

                    grid[y][x] = dist
