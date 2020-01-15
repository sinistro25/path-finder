from consts import *
def write_text(dsurf,text,pos):       
    text = FONT.render(text,True, TEXTCOLOR)
    text_rect = text.get_rect()
    text_rect.center = pos
    dsurf.blit(text,text_rect)