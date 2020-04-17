players = {"Red": 1, "Yellow": 2}


def check_U(grid, row, col):
    solution = [grid[row][col], grid[row - 1][col], grid[row - 2][col], grid[row - 3][col]]
    if max(solution) == min(solution):
        return solution[0]


def check_R(grid, row, col):
    solution = [grid[row][col], grid[row][col + 1], grid[row][col + 2], grid[row][col + 3]]
    if max(solution) == min(solution):
        return solution[0]


def check_UR(grid, row, col):
    solution = [grid[row][col], grid[row - 1][col + 1], grid[row - 2][col + 2], grid[row - 3][col + 3]]
    if max(solution) == min(solution):
        return solution[0]


def check_DR(grid, row, col):
    solution = [grid[row][col], grid[row + 1][col + 1], grid[row + 2][col + 2], grid[row + 3][col + 3]]
    if max(solution) == min(solution):
        return solution[0]


def checkWinner(grid):
    for row in range(5, -1, -1):
        for col in range(0, 7):
            if row >= 3:
                solution = check_U(grid, row, col)
                if col <= 3:
                    result2 = check_R(grid, row, col)
                    result3 = check_UR(grid, row, col)
            elif col <= 3:
                result2 = check_R(grid, row, col)
                result3 = check_DR(grid, row, col)
            if solution:
                return solution
            if result2:
                return result2
            if result3:
                return result3


def who_is_winner(moves):
    grid = [[0] * 7 for i in range(6)]
    for move in moves:
        col = ord(move[0]) - 65
        player = players[move[2:]]
        for row in range(5, -1, -1):
            if grid[row][col] == 0:
                grid[row][col] = player
                break
        solution = checkWinner(grid)
        if solution: return list(players)[list(players.values()).index(solution)]
    return "Draw"
