import os
from math import log
from functools import partial

N = 40 #40


def printM(M):
    for j in range(N):
        print([M[j*N+i] for i in range(N)])


# Quadrados são inteiros, index lineares. Devolve os quadrados a N,W,S,E
def adjacent(M,n):
    v = n//N
    res = ()
    for p in (N,-N):
        if 0 <= n+p < N*N and M[n+p] != 2:
            res += n+p,
    for p in (1,-1):
        if v*N <= n+p < (v+1)*N and M[n+p] != 2:
            res += n+p,
    return res


# Heap Operations
# Heaps são implementados com listas 1D
parent = lambda i: (i-1)//2
children = lambda i: (2*i+1, 2*i+2)


def heapAdd(heap, e):
    if log(len(heap)+1, 2).is_integer():
        heap += [-1, -1]
        heap[-2] = e
    else:
        for i,n in enumerate(heap):
            if n == -1:
                heap[i] = e
                break

def heapPop(heap):
    pop = heap[0]
    if log(len(heap)+1, 2).is_integer():
        i = len(heap) - 1
    else:
        for i,n in enumerate(heap):
            if n == -1:
                if i%2 == 0:
                    i -= 1
                else:
                    i += 1
    while True:
        p = parent(i) 
        # r/estofthefuckingowl
    






# BFS não recursivo utilizando uma Queue
def bfs(M, start, end):
    pred = [-1 for _ in range(N*N)]
    adj_history = []
    M[start] = 1
    q = [start]
    while len(q):
        v = q.pop(0)
        if v == end:
            return pred, adj_history
        for e in adjacent(M, v):
            if M[e] == 0:
                M[e] = 1
                pred[e] = v
                q.append(e)
                adj_history.append(e)
    return [], adj_history


def dfs(M, start, end):
    pred = [-1 for _ in range(N*N)]
    adj_history = []
    stack = [start]
    while len(stack):
        v = stack.pop(0)
        if v == end:
            return pred, adj_history
        if M[v] != 1:
            M[v] = 1
            for e in adjacent(M,v):
                stack = [e] + stack
                pred[e] = v
                adj_history.append(e)
    return [], adj_history


# A* - heap
def astar(M, start, end):
    open = [start]
    closed = []
    pred = [-1 for _ in range(N*N)]
    g = [-1 for _ in range(N*N)]
    g[start] = 0
    f = [-1 for _ in range(N*N)]
    f[start] = 1
    while len(open):
        return




# Devolve o caminho do inicio ao fim, independentemente do algoritmo utilizado
def crawlback(pred, end):
    if not len(pred):
        return []
    path = []
    i = end
    while pred[i] != -1:
        path.append(pred[i])
        i = pred[i]
    path = path[::-1]
    return path[1:]

