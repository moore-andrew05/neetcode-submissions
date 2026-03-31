class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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
        
        max_area = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    continue

                curr_area = 0
                q = deque([(y, x)])
                grid[y][x] = 0
                while q:
                    cury, curx = q.pop()
                    for ny, nx in get_neighbors(cury, curx):
                        if grid[ny][nx] == 1:
                            q.append((ny, nx))
                            grid[ny][nx] = 0
                    curr_area += 1
                max_area = max(curr_area, max_area)

        return max_area


'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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

        num_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "0":
                    continue
                
                q = deque([(y, x)])
                while q:
                    cury, curx = q.pop()
                    for ny, nx in get_neighbors(cury, curx):
                        if grid[ny][nx] == "1":
                            q.append((ny, nx))
                            grid[ny][nx] = "0"
                num_islands += 1

        return num_islands
'''                    
                        


                
 