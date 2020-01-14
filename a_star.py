from queue import PriorityQueue
from consts import * 
class ASTAR:
    
    def __init__(self,board):
        self.q = PriorityQueue()
        self.board = board
        self.back_board = [[None for i in range(board.w)] for j in range(board.h)]
        adj = board.adjacency(board.begin)
        self.done = False
        for x in adj:
            tile = board.get(x)
            if tile == Tile.BLANK:
                self.board.visiting(x)
                d = self.l1(self.board.end,x)
                self.q.put((1+d,d,x,1))
            elif tile == Tile.END:
                self.backup(x,node)
                self.backtrack()
                self.done = True
    
    def backup(self,pos,back):
        x,y = pos
        self.back_board[y][x] = back
    
    def l1(self,pos,dest):
        return abs(pos[0] - dest[0]) + abs(pos[1] - dest[1])
    
    def backtrack(self):
        curr = self.board.end
        while curr != None:
            x,y = curr
            curr = self.back_board[y][x]
            if curr is not None:
                self.board.pathfy(curr)
    
    def next(self):
        if self.done or self.q.empty():
            return True
        _,_,node,dist = self.q.get()
        self.board.visit(node)
        adj = self.board.adjacency(node)
        for x in adj:
            tile = self.board.get(x)
            if tile == Tile.BLANK:
                self.backup(x,node)
                self.board.visiting(x)
                d =self.l1(x,self.board.end)
                self.q.put((dist+d,d,x,dist+1))
            elif tile == Tile.END:
                self.backup(x,node)
                self.backtrack()
                self.done = True
                return True
        return False