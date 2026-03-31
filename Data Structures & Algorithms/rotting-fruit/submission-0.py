class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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

        fresh = set()
        rot = set()

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    rot.add((y, x))
                if grid[y][x] == 1:
                    fresh.add((y, x))

        time = 0
        while fresh:
            rot_spread = False
            q = deque(rot)

            while q:
                cury, curx = q.popleft()
                for ny, nx in get_neighbors(cury, curx):
                    if (ny, nx) in fresh:
                        fresh.remove((ny, nx))
                        rot.add((ny, nx))
                        rot_spread = True

            if not rot_spread:
                return -1
            time += 1
        return time

