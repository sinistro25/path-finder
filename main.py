import pygame
from board import Board
from pygame.locals import *
from consts import *
from bfs import BFS
from a_star import ASTAR
import time
import sys
from copy import deepcopy

if __name__ == "__main__":
    pygame.init()
    
    DSURF = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))
    board = Board(BOARDWIDTH,BOARDHEIGHT,100)
    board2 = deepcopy(board)
    board2.shift = BOARDWIDTH + 2
    a_star = ASTAR(board)
    bfs   = BFS(board2)
    DSURF.fill(Color.BLACK.value)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
        
        a_star.next()
        bfs.next()
        
        board.draw(DSURF)
        board2.draw(DSURF)
        
        pygame.display.update()
                
        time.sleep(1/FRAMERATE)