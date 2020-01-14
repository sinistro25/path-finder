import pygame
from board import Board
from pygame.locals import *
from consts import *
from bfs import BFS
from a_star import ASTAR
import time
import sys

if __name__ == "__main__":
    pygame.init()
    
    DSURF = pygame.display.set_mode((DISPLAYHEIGHT,DISPLAYWIDTH))
    board = Board(BOARDWIDTH,BOARDHEIGHT,130)
    #bfs   = BFS(board)
    a_star = ASTAR(board)
    DSURF.fill(Color.BLACK.value)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
        
        # bfs.next()
        a_star.next()
        board.draw(DSURF)
        
        pygame.display.update()
                
        time.sleep(1/FRAMERATE)