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
P.mixer.pre_init(22050,-16,2,64)
P.init()
JOY=[0,1,2,3]
def get_joystick():
    return JOY
def set_joystick(button,index):
    swap=1
    for i in range(4):
        if(swap and JOY[i]==button):
            JOY[i]=JOY[index]
            JOY[index]=button
            swap=0
    if(swap):
        JOY[index]=button
def music_play(mus,time=0):
    P.mixer.music.unload()
    try:
        P.mixer.music.load("ost/"+str(mus)+"I.ogg")
        P.mixer.music.queue("ost/"+str(mus)+"L.ogg",loops=-1)
        i=0
    except:
        P.mixer.music.load("ost/"+str(mus)+".ogg")
        i=-1
    P.mixer.music.play(start=time,loops=i)
def music_stop(fade):
    P.mixer.music.fadeout(int(fade*1000))
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
