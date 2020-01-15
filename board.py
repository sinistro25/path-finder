from consts import *
import random
import pygame.draw as pdraw
class Board:
    def __init__(self,w,h,num_blocks, shift_w=0, shift_h=TEXTHEIGHT):
        
        self.w = w
        self.h = h
        self.shift_w = shift_w
        self.shift_h = shift_h
        self.board = [Tile.BLANK if i + w*j >= num_blocks + 1 else Tile.BLOCK for i in range(w) for j in range(h)]
        self.board[0] = Tile.BEGIN
        self.board[1] = Tile.END
        random.shuffle(self.board)
        self.board = [[self.board[i + w*j] for i in range(w)] for j in range(h)]
        self.back_board = [[None for i in range(w)] for j in range(h)]
        
        for y in range(h):
            for x in range(w):
                tile = self.board[y][x]
                if tile == Tile.BEGIN:
                    self.begin = (x, y)
                elif tile == Tile.END:
                    self.end   = (x, y)

    
    def draw(self, dsurf):
        for y in range(self.h):
            for x in range(self.w):
                tile = self.board[y][x]
                if   tile == Tile.BLANK:
                    color =  Color.WHITE.value
                elif tile == Tile.BLOCK:
                    color =  Color.BLACK.value
                elif tile == Tile.VISITED:
                    color =  Color.GRAY.value
                elif tile == Tile.VISITING:
                    color =  Color.GREEN.value
                elif tile == Tile.FINISHED:
                    color =  Color.YELLOW.value
                elif tile == Tile.BEGIN:
                    color =  Color.BLUE.value
                elif tile == Tile.END:
                    color =  Color.YELLOW.value
                elif tile == Tile.PATH:
                    color =  Color.RED.value
                else:
                    throw(ValueError("Invalid Tile Enum"))
                pdraw.rect(dsurf, color, (BOXSIZE * (x + self.shift_w) + MARGIN, BOXSIZE * y + self.shift_h + MARGIN,TILESIZE,TILESIZE))
    
    def adjacency(self,pos):
        x,y = pos
        ladj = []
        if x < 0 or x > self.w or y < 0 or y > self.h:
            throw(ValueError(f"{pos} is out of bounds"))
        if x > 0:
            ladj.append((x-1,y))
        if y > 0:
            ladj.append((x,y-1))
        if x < self.w-1:
            ladj.append((x+1,y))
        if y < self.h-1:
            ladj.append((x,y+1))
        return ladj
    
    def get(self, pos):
        x,y = pos
        return self.board[y][x]
    
    def visit(self,pos):
        x,y = pos
        self.board[y][x] = Tile.VISITED
        
    def visiting(self, pos):
        x,y = pos
        self.board[y][x] = Tile.VISITING
    
    def pathfy(self,pos):
        x,y = pos
        self.board[y][x] = Tile.PATH
   