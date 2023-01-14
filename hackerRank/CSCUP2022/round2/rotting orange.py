def rotting(grid):
    # Write your code here
    grid_rows = len(grid)
    grid_columns = len(grid[0])

    def checkup(i, j):
        if i <= 0:
            return None
        if grid[i - 1][j] == 1:
            return [i-1, j]
        return None

    def checkdown(i, j):
        if i >= grid_rows - 1:
            return None
        if grid[i + 1][j] == 1:
            return [i+1, j]
        return None

    def checkright(i, j):
        if j >= grid_columns - 1:
            return None
        if grid[i][j + 1] == 1:
            return [i, j+1]

        return None

    def checkleft(i, j):
        if j <= 0:
            return None
        if grid[i][j - 1] == 1:
            return [i, j-1]
        return None


    def rotten(i, j):
        if grid[i][j] == 1:
            grid[i][j] = 2

    min = 0
    while True:
        moves = []
        flag = False
        for i in range(grid_rows):
            for j in range(grid_columns):
                cell = grid[i][j]

                if cell == 2:
                    up = checkup(i, j)
                    right = checkright(i, j)
                    left = checkleft(i, j)
                    down = checkdown(i, j)
                    if up != None: moves.append(up)
                    if right != None: moves.append(right)
                    if left != None: moves.append(left)
                    if down != None: moves.append(down)
                if cell == 1:
                    flag = True

        if flag and len(moves) == 0:
            min = -1
            break

        if len(moves) == 0:
            break

        for move in moves:
            rotten(move[0], move[1])

        min += 1


    return min