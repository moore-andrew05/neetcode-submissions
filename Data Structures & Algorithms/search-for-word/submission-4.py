class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        starting_coords = []
        dims = len(board), len(board[0])

        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val == word[0]:
                    starting_coords.append([y, x])

        def dfs(coords, i, word):
            if not (0 <= coords[0] < dims[0]) or\
            not (0 <= coords[1] < dims[1]) or\
            board[coords[0]][coords[1]] != word[i]:
                return False
            print("State")
            print(coords, board[coords[0]][coords[1]], i)
            
            if i == len(word) - 1:
                return True

            res = []

            board[coords[0]][coords[1]] = "#"

            for direction in directions:
                print("Making Move")
                print(coords, direction)
                res.append(dfs([coords[0] + direction[0], coords[1] + direction[1]], i + 1, word))
            for r in res:
                if r:
                    return True

            board[coords[0]][coords[1]] = word[i]
            return False


        for coords in starting_coords:
            if dfs(coords, 0, word):
                return True
            
        return False


        


