'''
Given a grid of 1 and 0, return number of contiguous sections of 1s.
    - Only cardinal directions (4)

Loop through each cell:

if 0:
- add to visited, continue

if 1:
- enqueue position
- add to visited
- Increment # islands


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
        visited = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) in visited or grid[y][x] == "0":
                    visited.add((y, x))
                    continue
                
                q = deque([(y, x)])
                while q:
                    cury, curx = q.pop()
                    if (cury, curx) in visited:
                        continue
                    visited.add((cury, curx))
                    if grid[cury][curx] == "0":
                        continue
                    for ny, nx in get_neighbors(cury, curx):
                        if (ny, nx) not in visited and grid[ny][nx] == "1":
                            q.append((ny, nx))
                num_islands += 1

        return num_islands
                    
                        


                
