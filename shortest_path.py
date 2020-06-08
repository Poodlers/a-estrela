import pygame
from tkinter import *
pygame.init()
#open a tkinter window asking for the dimensions of the grid, initial point and final point
def submit_data():
    clear_1 = Label(root, text="                                                                                                                            ")
    for i in [190,210,230]:
        clear_1.place(x = 5, y = i)
    error_msg = Label(root, text="You did't insert valid values for the grid!")
    error_msg2 = Label(root,text = "You wrote some non-integer value on the camps!")
    try:
        a = int(e1.get())
        b = int(e2.get())
        c = int(e3.get())
        d = int(e4.get())
        e = int(e5.get())
        f = int(e6.get())
    except:
        error_msg2.place(x = 10, y = 230)
    if int(e1.get()) not in range(1,80) or int(e2.get()) not in range(1,80):
        error_msg.place(x = 10, y = 190)
    else:
        error_msg.destroy()
    error_msg1 = Label(root, text = "You didn't insert valid values for the coordinates!")
    if int(e3.get()) < 0 or int(e3.get()) > int(e1.get()) or int(e4.get()) < 0 or int(e4.get()) > int(e2.get()) or int(e5.get()) < 0 or int(e5.get()) > int(e1.get()) or int(e6.get()) < 0 or int(e6.get()) > int(e2.get()):
        error_msg1.place(x = 10, y = 210)
    global values
    values = (int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get()), int(e6.get()),var1.get())
    root.destroy()


root = Tk()
Label(root, text="X size of grid").place(x = 10, y = 20)
Label(root, text="Y size of grid").place(x = 10, y = 50)
Label(root, text = "X_initial").place(x = 10, y = 80)
Label(root, text = "Y_initial").place(x = 170, y = 80)
Label(root, text = "X_final").place(x = 10, y = 110)
Label(root, text = "Y_final").place(x = 170, y = 110)
e1 = Entry(root)
e2 = Entry(root)

e3 = Entry(root, width = 10)
e3.place(x = 60, y= 80)

e4 = Entry(root, width = 10)
e4.place(x = 230, y= 80)
e5 = Entry(root, width = 10)
e5.place(x = 60, y = 110)
e6 = Entry(root, width = 10)

var1 = IntVar()
e7 = Checkbutton(root, text="Show Steps", variable=var1).place(x = 20, y = 150)
e6.place(x = 230, y= 110)
e1.place(x = 120, y = 20)
e2.place(x = 120, y = 50)
submit_button = Button(root, text = "Enter", command = submit_data)
submit_button.place(x = 180, y = 160)

root.geometry("400x250")
root.mainloop()

pygame.init()
run = True
win = pygame.display.set_mode((720,720))
pygame.display.set_caption("The Shortest Path")
win.fill((255,255,255))
grid = [[0 for i in range(values[0])] for a in range(values[1])]
grid[values[3]][values[2]] = 2
grid[values[5]][values[4]] = 3
def redraw_window():
    global grid
    win.fill((255,255,255))
    global values
    for i in range(0,values[0] + 1):
        pygame.draw.line(win, (0,0,0), (i*(720/values[0]),0), (i*(720/values[0]),720))
    for i in range(0,values[1] + 1):
        pygame.draw.line(win, (0,0,0), (0,i * (720/values[1])), (720,i * (720/values[1])))
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if grid[a][b] == 1:
                pygame.draw.rect(win, (0,0,0),(b*(720/values[1]),a*(720/values[0]),720/values[0],720/values[1]))
            if grid[a][b] == 2:
                pygame.draw.rect(win, (0, 255, 0),(b * (720 / values[1]), a * (720 / values[0]), 720 / values[0], 720 / values[1]))
            elif grid[a][b] == 3:
                pygame.draw.rect(win, (0, 0, 255),(b * (720 / values[1]), a * (720 / values[0]), 720 / values[0], 720 / values[1]))
            if grid[a][b] == "#":
                pygame.draw.rect(win, (255, 0, 0),(b * (720 / values[1]), a * (720 / values[0]), 720 / values[0], 720 / values[1]))
def make_block_unpassable(mouse):
    global grid
    for i in range(0, values[0]):
        if i * (720/values[0]) > mouse[0]:
            rect_x = (i - 1)
            break
        if i == values[0] - 1:
            rect_x = i
    for j in range(0, values[1]):
        if j * (720/values[1]) > mouse[1]:
            rect_y = (j - 1)
            break
        if j == values[1] - 1:
            rect_y = j
    if grid[rect_y][rect_x] == 1:
        grid[rect_y][rect_x] = 0
    elif grid[rect_y][rect_x] == 0:
        grid[rect_y][rect_x] = 1


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
    for i in [(0,1),(0,-1),(1,0),(-1,0)]:
        if current[0] + i[0] > len(grid[0]) - 1 or current[0] + i[0] < 0 or current[1] + i[1] > len(grid) - 1 or current[1] + i[1] < 0:
            continue
        if grid[current[0] + i[0]][current[1] + i[1]] == 1:
            continue
        if (current[0] + i[0], current[1] + i[1]) in CLOSED:
            continue
        neighbours.append([(current[0] + i[0], current[1] + i[1]),0,0,0])
    return neighbours

def retrace_path(start, end):
    global grid
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node[0])
        if grid[current_node[0][0]][current_node[0][1]] != 3:
            grid[current_node[0][0]][current_node[0][1]] = "#"
        current_node = current_node[3]

def shortest_path():
    font = pygame.font.Font('freesansbold.ttf', 17)
    global OPEN
    global CLOSED
    global start_node
    while len(OPEN) > 0:
        current = OPEN[0]
        for i in OPEN:
            if i[1] + i[2] < current[1] + current[2] or ((i[1] + i[2] == current[1] + current[2]) and i[2] < current[2]):
                current = i
        OPEN.remove(current)
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
    if len(OPEN) == 0:
        text = font.render("There is no path to the destination!",True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (360,360)
        win.blit(text,text_rect)
        pygame.display.update()
        OPEN = []
        CLOSED = []
        OPEN.append(start_node)
        pygame.time.delay(3000)


while run == True:

    pygame.time.delay(50)
    redraw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                shortest_path()
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()

            make_block_unpassable(mouse)


    pygame.display.update()