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

