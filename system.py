class ObjectGroup():
    def __init__(self):
        self._object=[]
    def add(self,obj):
        self._object.append(obj)
    def kill(self,obj):
        self._object.remove(obj)
    def update(self,CON,BGO,HUD):
        for i in self._object:
            i.update(CON,BGO,HUD)
    def draw(self,DISPLAY,TICK):
        for i in self._object:
            i.draw(DISPLAY,TICK)
def clamp(n,min,max):
    if n<min:
        return min
    elif n>max:
        return max
    return n
import pygame as P
P.init()
MUS_PLAYED=0
MUS_LOOP=0
MUS_TIME=0
def music_load(mus):
    global MUS_LOOP,MUS_TIME,MUS_PLAYED
    if mus!="Cirno Stage":
        MUS_LOOP=0.67+1.2
        MUS_TIME=64.6+1.2
    P.mixer.music.unload()
    P.mixer.music.load("ost/"+str(mus)+".mp3")
def music_play(time=0):
    global MUS_PLAYED
    MUS_PLAYED=time
    P.mixer.music.play(start=time)
def music_stop(fade):
    P.mixer.music.fadeout(int(fade*1000))
def update_music():
    global MUS_LOOP,MUS_TIME,MUS_PLAYED
    if P.mixer.music.get_pos()/1000>MUS_TIME-MUS_PLAYED+0.07:
        music_play(time=MUS_LOOP)
FONT=[]
FONT.append(P.font.Font("font/NES.ttf",8))
FONT.append(P.font.Font("font/TH6.ttf",16))
def draw_text(text,pos,DISPLAY,color=(255,255,255),font=0,align=0,mode=0):
    i=FONT[font].render(text,1,(0,0,0))
    pos=(pos[0]-(align*i.get_width())/2,pos[1])
    #border
    DISPLAY.blit(i,(pos[0]+1,pos[1]))
    DISPLAY.blit(i,(pos[0],pos[1]+1))
    DISPLAY.blit(i,(pos[0]-1,pos[1]))
    DISPLAY.blit(i,(pos[0],pos[1]-1))
    #shadow
    i.set_alpha(40)
    DISPLAY.blit(i,(pos[0]+2,pos[1]))
    DISPLAY.blit(i,(pos[0]+2,pos[1]+1))
    DISPLAY.blit(i,(pos[0],pos[1]+2))
    DISPLAY.blit(i,(pos[0]+1,pos[1]+2))
    DISPLAY.blit(i,(pos[0]+2,pos[1]+2))
    #color
    i=FONT[font].render(text,1,color)
    c=P.Surface(i.get_size(),depth=32)
    h=170/i.get_height()
    if(mode==0):
        for y in range(i.get_height()):
            P.draw.line(c,(y*h,y*h,y*h),(0,y),(i.get_width(),y))
        i.blit(c,(0,0),special_flags=P.BLEND_SUB)
    elif(mode==1):
        for y in range(i.get_height()):
            P.draw.line(c,(y*h,y*h,y*h),(0,y),(i.get_width(),y))
        i.blit(c,(0,0),special_flags=P.BLEND_ADD)
    elif(mode==2):
        for y in range(i.get_height()):
            P.draw.line(c,(255-y*h,255-y*h,255-y*h),(0,y),(i.get_width(),y))
        i.blit(c,(0,0),special_flags=P.BLEND_SUB)
    elif(mode==3):
        for y in range(i.get_height()):
            P.draw.line(c,(255-y*h,255-y*h,255-y*h),(0,y),(i.get_width(),y))
        i.blit(c,(0,0),special_flags=P.BLEND_ADD)
    DISPLAY.blit(i,pos)
