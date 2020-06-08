import queue
grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 2, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3]]

values = (0,0,2,2,6,6)
def valid(grid,moves):
    global values
    visited = [[False for i in range(0, len(grid[0]))] for z in range(0, len(grid))]
    i = values[2]
    j = values[3]
    visited[j][i] = True
    for move in moves:
        if move == "L":
            i -= 1
        if move == "R":
            i += 1
        if move == "U":
            j -= 1
        if move == "D":
            j += 1

        if i > len(grid[0]) - 1 or i < 0 or j < 0 or j > len(grid) - 1: #out of bounds
            return False
        if visited[j][i]:
            return False
        visited[j][i] = True
        if grid[j][i] == 1:
            return False

    return True
def printMaze(grid,moves):
    global values
    i = values[2]
    j = values[3]
    pos = []
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        pos.append((j,i))
        print(pos)
    for i in pos:
        grid[i[0]][i[1]] = "#"
    print(grid)
def findEnd(grid,moves):
    global values
    i = values[2]
    j = values[3]
    for move in moves:
        if move == "L":
            i -= 1
        if move == "R":
            i += 1
        if move == "U":
            j -= 1
        if move == "D":
            j += 1
        if grid[j][i] == 3:
            printMaze(grid,moves)
            return True
    return False

def solve():
    global grid
    global values
    nums = queue.Queue()
    nums.put("")
    add = ""
    while not findEnd(grid,add):
        add = nums.get()
        for j in ["L","R","U","D"]:
            put = add + j
            if valid(grid,put):
                nums.put(put)



print(solve())