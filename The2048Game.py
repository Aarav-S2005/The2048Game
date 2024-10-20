import random as rd
import sys
from tkinter import *
from tkinter import messagebox as mb

score = 0
game_started = False
labels = []
color_of_each_number = {0: "#cdc1b4", 2: "#faefe3", 4: "#ede0c8", 8: "#e69a49", 16: "#e67905", 32: "#f5600a", 64: "#ff4405", 128: "#f1d26d", 256:"#f2d366", 512:"#edc651", 1024:"#eec744", 2048:"#ecc230"}

root = Tk()
root.title("2048")

sc = Canvas(root, background="#bbaea0", width=480, height=600)
sc.pack()

heading = Label(root, background="#bbaea0", text="2048 Game", font=("comic sans ms", 27, "bold"))
sc.create_window( 240, 60, window=heading)

score_label = Label(root, background="#bbaea0", text=f"score:{score}", font=("comic sans ms", 16, "bold"))
sc.create_window(240, 105, window=score_label)

grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(4):
    label_d = {}
    for j in range(4):
        label_d[f'l{i}{j}'] = Label(root, background="#cdc1b4", text=" ", font=("comic sans ms", 20), bd=2, relief="solid", padx=48, pady=34, )
        sc.create_window(60+i*120, 180+j*120, window=label_d[f'l{i}{j}'])
    labels.append(label_d)

def start_game(_):
    global color_of_each_number, labels, game_started
    if not game_started:
        x1 = rd.choice(range(4))
        y1 = rd.choice(range(4))
        x2 = rd.choice(range(4))
        y2 = rd.choice(range(4))
        while x1==x2 or y1==y2:
            x2 = rd.choice(range(4))
            y2 = rd.choice(range(4))
        grid[y1][x1] = 2
        grid[y2][x2] = 2
        labels[x1][f"l{x1}{y1}"].config(text = "2", bg = color_of_each_number[2], padx = 44)
        labels[x2][f"l{x2}{y2}"].config(text = "2", bg = color_of_each_number[2], padx = 44)
        game_started = True

def update_label():
    global labels, grid, score_label, score, sc
    score_label.config(text=f"score:{score}")
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if grid[i][j]<10:
                    labels[j][f"l{j}{i}"].config(text=str(grid[i][j]), bg=color_of_each_number[grid[i][j]], padx =44)
                elif grid[i][j]<100:
                    labels[j][f"l{j}{i}"].config(text=str(grid[i][j]), bg=color_of_each_number[grid[i][j]], padx =36)
                elif grid[i][j]<1000:
                    labels[j][f"l{j}{i}"].config(text=str(grid[i][j]), bg=color_of_each_number[grid[i][j]], padx =28)
                elif grid[i][j]<999:
                    labels[j][f"l{j}{i}"].config(text=str(grid[i][j]), bg=color_of_each_number[grid[i][j]], padx =20)
            else:
                labels[j][f"l{j}{i}"].config(text=" ", bg=color_of_each_number[0], padx = 48)

def check_for_same_neighbour_in_the_grid(grid) -> bool:
    for i in range(4):
        for j in range(4):
            if i%3 == 0 and j%3 == 0:
                continue
            elif i == 0 :
                if grid[i][j] in [grid[i][j-1], grid[i][j+1], grid[i+1][j]]:
                    return False
            elif i == 3:
                if grid[i][j] in [grid[i][j - 1], grid[i][j + 1], grid[i - 1][j]]:
                    return False
            elif j == 0:
                if grid[i][j] in [grid[i-1][j], grid[i][j + 1], grid[i + 1][j]]:
                    return False
            elif j == 3:
                if grid[i][j] in [grid[i-1][j ], grid[i][j - 1], grid[i + 1][j]]:
                    return False
            else:
                if grid[i][j] in [grid[i][j - 1], grid[i][j + 1], grid[i + 1][j], grid[i-1][j]]:
                    return False
    return True

def check_game_over():
    global grid, score, labels, score_label, game_started
    game_over = False

    if not any(0 in row for row in grid) and check_for_same_neighbour_in_the_grid(grid):
        game_over = True
        
    if any(2048 in row for row in grid):
        mb.showinfo("Yayy!!", f"CONGRATULATIONS!!\nYou won with {score} points")
        grid = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        score = 0
        score_label.config(text=f"score:{score}")
        update_label()
        game_started = False
        return 

    if not game_over:
        return
    else:
        mb.showinfo("Game Over", "GAME OVER!\nThere are no possible moves now")
        grid = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        score = 0
        score_label.config(text=f"score:{score}")
        update_label()
        game_started = False

def random_popup_num():
    return rd.choice(([2] * 7) + ([4]*3))

def add_num():
    global grid, labels, color_of_each_number
    num = random_popup_num()
    x = rd.choice(range(4))
    y = rd.choice(range(4))
    while grid[x][y]!=0:
        x = rd.choice(range(4))
        y = rd.choice(range(4))
    grid[x][y] = num
    labels[y][f"l{y}{x}"].config(text=num, background=color_of_each_number[num], padx =48 - (4 * len(str(grid[j][i]))))

def left_click( grid):
    global labels, color_of_each_number,  score, game_started
    if not game_started:
        return
    initial = list(list())
    for i in grid:
        initial.append(i[:])

    for i in range(4):
        for k in range(4):
            for j in range(3):
                if grid[i][j] == grid[i][j+1] :
                    grid[i][j] *= 2
                    grid[i][j+1] = 0
                    score+= grid[i][j]
                elif grid[i][j] == 0:
                    grid[i][j] = grid[i][j+1]
                    grid[i][j + 1] = 0
    update_label()
    if grid != initial:
        add_num()
    check_game_over()
    # print(grid)

def right_click(grid):
    global labels, color_of_each_number, score, game_started
    if not game_started:
        return
    initial = list(list())
    for i in grid:
        initial.append(i[:])

    for i in range(4):
        for k in range(4):
            for j in range(3, 0, -1):
                if grid[i][j] == grid[i][j - 1]:
                    grid[i][j] *= 2
                    grid[i][j - 1] = 0
                    score+=grid[i][j]
                elif grid[i][j] == 0:
                    grid[i][j] = grid[i][j - 1]
                    grid[i][j - 1] = 0
    update_label()
    if grid != initial:
        add_num()
    check_game_over()
    #print(grid)

def down_click(grid):
    global labels, color_of_each_number, score, game_started
    if not game_started:
        return
    initial = list(list())
    for i in grid:
        initial.append(i[:])
    for j in range(4):
        for k in range(4):
            for i in range(3, 0, -1):
                if grid[i][j] == grid[i - 1][j]:
                    grid[i][j] *= 2
                    grid[i - 1][j] = 0
                    score+=grid[i][j]
                elif grid[i][j] == 0:
                    grid[i][j] = grid[i - 1][j]
                    grid[i - 1][j] = 0
    update_label()
    if grid != initial:
        add_num()
    check_game_over()
    # print(grid)

def up_click(grid):
    global labels, color_of_each_number, score, game_started
    if not game_started:
        return
    initial = list(list())
    for i in grid:
        initial.append(i[:])

    for j in range(4):
        for k in range(4):
            for i in range(3):
                if grid[i][j] == grid[i+1][j] :
                    grid[i][j] *= 2
                    grid[i+1][j] = 0
                    score+=grid[i][j]
                elif grid[i][j] == 0:
                    grid[i][j] = grid[i+1][j]
                    grid[i+1][j] = 0
    update_label()
    if grid != initial:
        add_num()
    check_game_over()
    # print(grid)

def exitfunc(_):
    root.destroy()
    sys.exit()

root.bind("<Right>", lambda _: right_click(grid))
root.bind("<Left>", lambda _: left_click(grid))
root.bind("<Down>", lambda _: down_click(grid))
root.bind("<Up>", lambda _: up_click(grid))
root.bind("<space>", start_game)
root.bind("<Escape>", exitfunc)

mainloop()
