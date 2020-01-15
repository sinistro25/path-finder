from enum import Enum,auto

class Tile(Enum):
    
    BLANK    = auto()
    BLOCK    = auto()
    BEGIN    = auto()
    END      = auto()
    VISITED  = auto()
    VISITING = auto()
    FINISHED = auto()
    PATH     = auto()

class Color(Enum):
    
    WHITE  = (255,255,255)
    BLACK  = (  0,  0,  0)
    RED    = (255,  0,  0)
    GREEN  = (  0,255,  0)
    BLUE   = (  0,  0,255)
    YELLOW = (255,255,  0)
    GRAY   = (128,128,128)
    PURPLE = ( 61,0  , 96)

TILESIZE    = 30
MARGIN      = 3
BOXSIZE     = TILESIZE + MARGIN
BOARDWIDTH  = 20
BOARDHEIGHT = 20
FRAMERATE   = 30

DISPLAYWIDTH  = 2 * BOXSIZE * BOARDWIDTH + MARGIN + 2 * BOXSIZE
DISPLAYHEIGHT = BOXSIZE * BOARDHEIGHT + MARGIN


