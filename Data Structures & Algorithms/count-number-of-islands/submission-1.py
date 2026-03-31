class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dims = len(grid), len(grid[0])
        visited = [[0] * dims[1] for _ in range(dims[0])]
        num_islands = 0
        
        def is_valid(x, y):
            return (x >= 0) and (y >= 0) and (x < dims[1]) and (y < dims[0])

        for y_start in range(dims[0]):
            for x_start in range(dims[1]):
                if visited[y_start][x_start] == 1 or grid[y_start][x_start] == '0':
                    continue
                
                starting_coord = [x_start, y_start]
                queue = [ starting_coord ]
                tile_type = grid[y_start][x_start]
                num_islands += 1
               

                visited[starting_coord[1]][starting_coord[0]] = 1


                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                while queue:
                    x, y = queue.pop(0)

                    for direction in directions:
                        new_x = x + direction[1]
                        new_y = y + direction[0]


                        if is_valid(new_x, new_y) and visited[new_y][new_x] == 0 and grid[new_y][new_x] == tile_type:
                            visited[new_y][new_x] = 1
                            queue.append([new_x, new_y])

        return num_islands