import pygame
class Blits:
    def button_blit(text:str,pos:tuple,width:int,height:int,font_size:int):
        font = pygame.font.SysFont("Futura", font_size)
        text_blit = font.render(text, True, (0, 0, 0))
        render_list = {"text":[],"button":[],"rectangle":[]}
        render_list["text"].append((text_blit,(pos[0]+10,pos[1]+10)))
        render_list["button"].append((text,(pos[0]+10,pos[1]+10,width-20,height-20)))
        render_list["rectangle"].append(((0,0,0),(pos[0],pos[1],width,height)))
        render_list["rectangle"].append(((255,255,255),(pos[0]+10,pos[1]+10,width-20,height-20)))
        return render_list