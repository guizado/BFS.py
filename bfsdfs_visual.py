import tkinter as tk
from PIL import ImageTk, Image
from bfsdfs_aux import *
import random

DELTA_TIME = 2 #ms
N = 40

root = tk.Tk()
root.geometry('700x700')
frame = tk.Frame(root, width=400, height=400,bg='gray')
frame.place(relx=0.5,rely=0.5,anchor='center')


white = ImageTk.PhotoImage(Image.open("squares/white_square.png"))
black = ImageTk.PhotoImage(Image.open("squares/black_square.png")) 
blue0 = ImageTk.PhotoImage(Image.open("squares/blue0_square.png")) 
blue1 = ImageTk.PhotoImage(Image.open("squares/blue1_square.png")) 
orange = ImageTk.PhotoImage(Image.open("squares/orange_square.png")) 
yorange = ImageTk.PhotoImage(Image.open("squares/yelloworange_square.png")) 
orange2 = ImageTk.PhotoImage(Image.open("squares/orange2_square.png")) 


M = [0 for _ in range(N*N)]
squares = []
start = None
end = None


def erase_all():
    global start, end, M
    for i in range(1600):
        squares[i].configure(image=white)
        squares[i].unbind("<B1-Motion>")
        squares[i].bind("<1>", partial(define_start_end, i))
    start = None
    end = None
    M = [0 for _ in range(N*N)]


def define_start_end(i, event):
    global start, end
    if start == None:
        squares[i].configure(image=orange)
        start = i
    elif end == None:
        if i != start:
            squares[i].configure(image=orange)
            end = i
            for x in range(N*N):
                squares[x].unbind('<1>')
                squares[x].bind("<B1-Motion>", partial(w2b,x))
            squares[start].unbind("<B1-Motion>")
            squares[end].unbind("<B1-Motion>")
            bfsB['state'] = 'normal'
            randomWallsB['state'] = 'normal'


def w2b(i, event):
    global M
    M[i] = 2
    squares[i].configure(image=black)
    if event:
        w = event.widget.winfo_containing(event.x_root, event.y_root)
        if w:
            w.event_generate("<B1-Motion>")


def random_walls():
    for _ in range(500):
        r = random.randint(0,N*N-1)
        if r != start and r != end:
            w2b(r, None)


def animation(adj_history, path):
    def trace_path(path):
        for p in path:
            squares[p].configure(image=orange2)
    if len(adj_history) and adj_history[0] != end:
            squares[adj_history[0]].configure(image=blue0)
    else:
        trace_path(path)
        return
    root.after(DELTA_TIME, lambda:animation(adj_history[1:], path))


def start_bfs():
    pred, adj_history = bfs(M, start, end)
    path = crawlback(pred, end)
    animation(adj_history, path)
    bfsB['state'] = 'disabled'
    randomWallsB['state'] = 'disabled'



eraser = tk.Button(root, text='Erase', command=erase_all)
eraser.place(relx=0.5, rely=0.95, anchor='center')
bfsB = tk.Button(root, text ='BFS', state='disabled', command=start_bfs)
bfsB.place(relx=0.2, rely=0.95, anchor='center')
randomWallsB = tk.Button(root, text ='Random', state='disabled', command=random_walls)
randomWallsB.place(relx=0.8, rely=0.95, anchor='center')


for i,c in enumerate([(x,y) for x in range(40) for y in range(40)]):
    squares.append(tk.Label(frame, image=white, relief='sunken'))
    squares[-1].grid(row=c[0], column=c[1])
    squares[-1].bind("<1>", partial(define_start_end,i))


root.mainloop()
