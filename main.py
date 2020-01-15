import pygame
from board import Board
from pygame.locals import *
from consts import *
from bfs import BFS
from a_star import ASTAR
import time
import sys
from copy import deepcopy

def write_text(text,pos):       
    text = FONT.render(text,True, TEXTCOLOR)
    text_rect = text.get_rect()
    text_rect.center = pos
    DSURF.blit(text,text_rect)

if __name__ == "__main__":
    pygame.init()
    
    DSURF = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))
    
    board = Board(BOARDWIDTH,BOARDHEIGHT,100)
    board2 = deepcopy(board)
    board2.shift_w = BOARDWIDTH + 2
    
    a_star = ASTAR(board)
    bfs   = BFS(board2)
    
    iter_star = 1
    iter_bfs = 1   
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
        
        if not a_star.next():
            iter_star += 1 
        if not bfs.next():
            iter_bfs  += 1
        
        DSURF.fill(Color.BLACK.value)        

        board.draw(DSURF)
        board2.draw(DSURF)
        
        write_text("A*" , (BOXSIZE*BOARDWIDTH/2,TEXTHEIGHT/2))
        write_text("BFS", (1.5*BOXSIZE*(BOARDWIDTH+1),TEXTHEIGHT/2))
        write_text(f"Iterations ={iter_star: 3d}" , (BOXSIZE*BOARDWIDTH/2, BOXSIZE*BOARDHEIGHT + 1.5*TEXTHEIGHT))
        write_text(f"Iterations ={iter_bfs: 3d}", (1.5*BOXSIZE*(BOARDWIDTH+1),    BOXSIZE*BOARDHEIGHT + 1.5*TEXTHEIGHT))

        
        pygame.display.update()
                
        time.sleep(1/FRAMERATE)