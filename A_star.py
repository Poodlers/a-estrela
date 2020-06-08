
values = (0,0,2,2,6,6)
grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 2, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3]]
OPEN = []
CLOSED = []

def get_distance(pos1,pos2):
    distX = abs((pos1[0] - pos2[0]))
    distY = abs((pos1[1] - pos2[1]))
    if distX > distY:
        return 14* distY + 10 *(distX - distY)
    else:
        return 14*distX + 10 *(distY - distX)

start_node = [(values[3],values[2]), 0 , get_distance((values[3],values[2]), (values[5],values[4]) ), 0 ]
OPEN.append(start_node)
def neighbours(current):
    global grid
    neighbours = []
    for i in [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,1),(-1,-1)]:
        if current[0] + i[0] > len(grid[0]) - 1 or current[0] + i[0] < 0 or current[1] + i[1] > len(grid) - 1 or current[1] + i[1] < 0:
            continue
        if grid[current[0] + i[0]][current[1] + i[1]] == 1:
            continue
        if (current[0] + i[0], current[1] + i[1]) in CLOSED:
            continue
        neighbours.append([(current[0] + i[0], current[1] + i[1]),0,0, 0 ])
        return neighbours
def retrace_path(start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node[0])
        current_node = current_node[3]
    path.reverse()
    print(path)



while len(OPEN) > 0:
    current = OPEN[0]
    for i in OPEN:
        if i[1] + i[2] < current[1] + current[2] or ((i[1] + i[2] == current[1] + current[2]) and i[2] < current[2]):
            current = i
        OPEN.remove(current)
        print(current)
        CLOSED.append(current[0])
        if current[0] == (values[5],values[4]):
            retrace_path(start_node, current)
            break
        for i in neighbours(current[0]):
            MovementCostToNeighbour = current[1] + get_distance(current[0], i[0])
            if MovementCostToNeighbour < i[1] or i not in OPEN:
                i[1] = MovementCostToNeighbour
                i[2] = get_distance(i[0], (values[5],values[4]))
                i[3] = current
                if i not in OPEN:
                    OPEN.append(i)


