class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check_valid(y, x):
            if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):
                return True
            return False

        def get_valid_next_steps(y, x):
            DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
            valid = []

            for dy, dx in DIRS:
                newy = y + dy
                newx = x + dx
                if check_valid(newy, newx):
                    valid.append((newy, newx))
            
            return valid
                


        starting_coords = []

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    starting_coords.append((y, x))


        for y, x in starting_coords:
            stk = deque([[(y, x), 0, set(), word[0]]])

            while stk:
                coords, curr_pos, visited, curr_word = stk.pop()
                visited.add(coords)
                if curr_pos == len(word) - 1:
                    return True

                checks = get_valid_next_steps(*coords)
                for y, x in checks:
                    if board[y][x] == word[curr_pos + 1] and (y, x) not in visited:
                        stk.append([(y, x), curr_pos + 1, visited.copy(), curr_word + board[y][x]])

        return False

                

                




                     

