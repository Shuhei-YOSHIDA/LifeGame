#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def cellOnCheck(world, x, y):
    res = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if world[x+i][y+j] == True:
                res = res + 1
    
    if world[x][y] == True:
        if res == 2 or res == 3:
            return True
        else :
            return False
    else:
        if res == 3:
            return True
        else :
            return False


def nextgen(world):
    # World size check
    row, col = world.shape
    newWorld = np.zeros([row,col], dtype=np.bool)

    # Read each cell
    for i in range(1, row-1):
        for j in range(1, col-1):
            newWorld[i][j] = cellOnCheck(world, i, j)

    return newWorld

def lifegame(iterative=30):
    height = 40
    width = 50
    world = np.zeros([height+2, width+2], dtype=np.bool) ## with wall
    #world[2:15][4] = True # tekitou

    # blinker
    for i in range(4):
        for j in range(3):
            world[j+10][10*i+5] = True
        for j in range(3):
            world[9][10*i+10+j] = True

    # 10-line
    for i in range(10):
        world[30][20+i] = True
        

    #while True:
    yield world # initial world
    for i in range(iterative):
        world = nextgen(world)
        yield world

def printWorld(world):
    row, col = world.shape
    x = np.zeros(row*col)
    y = np.zeros(row*col)
    #x = []
    #y = []

    cnt = 0
    for i in range(1,row-1):
        for j in range(1,col-1):
            if world[i][j] == True:
                x[cnt] = i
                y[cnt] = j
                #x.append(i)
                #y.append(j)
                cnt = cnt + 1

    #im = plt.scatter(x,y)
    im = plt.scatter(y[0:cnt], x[0:cnt], s=50, c="pink", alpha=0.5, linewidths="2", edgecolors="red")
    return im



if __name__ == '__main__':
    print 'life game'
    fig = plt.figure()
    plt.axis('equal')
    plt.xlim(0,55)
    plt.ylim(0,55)
    ims = []
    for x in lifegame():
        ims.append([printWorld(x)])

    ani = animation.ArtistAnimation(fig, ims, interval=500)
    ani.save('lifegame.gif', writer='imagemagick')
    plt.show()

