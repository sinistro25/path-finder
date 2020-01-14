from queue import Queue
from consts import * 
class BFS:
    
    def __init__(self,board):
        self.q = Queue()
        self.board = board
        self.back_board = [[None for i in range(board.w)] for j in range(board.h)]
        adj = board.adjacency(board.begin)
        for x in adj:
            self.board.visiting(x)
            self.q.put(x)
        self.done = False
    
    def backup(self,pos,back):
        x,y = pos
        self.back_board[y][x] = back
    
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
        node = self.q.get()
        self.board.visit(node)
        adj = self.board.adjacency(node)
        for x in adj:
            tile = self.board.get(x)
            if tile == Tile.BLANK:
                self.backup(x,node)
                self.board.visiting(x)
                self.q.put(x)
            elif tile == Tile.END:
                self.backup(x,node)
                self.backtrack()
                self.done = True
                return True
        return False