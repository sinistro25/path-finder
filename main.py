import time
import sys

from copy import deepcopy
import pygame
from pygame.locals import *

from board import Board
from consts import *
from text import *
from bfs import BFS
from a_star import ASTAR



if __name__ == "__main__":
    # Create GUI window
    pygame.init()
    DSURF = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))
    
    # Create the gridworld where the search will take place
    board = Board(BOARDWIDTH,BOARDHEIGHT,100)
    board2 = deepcopy(board)
    board2.shift_w = BOARDWIDTH + 2
    
    # Initialize the BFS and A* graph search algorithms
    a_star = ASTAR(board)
    bfs   = BFS(board2)
    
    # Counter for the number of iterations the algorithm have taken
    iter_star = 1
    iter_bfs = 1   
    
    while True:
        
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
                
        # Count the number of iterations
        if not a_star.next():
            iter_star += 1 
        if not bfs.next():
            iter_bfs  += 1
        
        # Clear the display
        DSURF.fill(Color.BLACK.value)        
        
        # Draw the boards
        board.draw(DSURF)
        board2.draw(DSURF)
        
        # Write the display information
        write_text(DSURF, "A*" , (BOXSIZE*BOARDWIDTH/2,TEXTHEIGHT/2))
        write_text(DSURF, "BFS", (1.5*BOXSIZE*(BOARDWIDTH+1),TEXTHEIGHT/2))
        write_text(DSURF, f"Iterations ={iter_star: 3d}" , (BOXSIZE*BOARDWIDTH/2, BOXSIZE*BOARDHEIGHT + 1.5*TEXTHEIGHT))
        write_text(DSURF, f"Iterations ={iter_bfs: 3d}", (1.5*BOXSIZE*(BOARDWIDTH+1),    BOXSIZE*BOARDHEIGHT + 1.5*TEXTHEIGHT))

        # Draw changes to the GUI window
        pygame.display.update()
        
        # Limit the number of iterations per second to less or equal then FRAMERATE
        # This is a poor implementation since it doesn't account to the variation due to the 
        # search algorithm time not beign accounted but works well enough for this case
        time.sleep(1/FRAMERATE)