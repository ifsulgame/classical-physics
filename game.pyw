try:
    import pygame as P
except:
    print("pygame ins't install\npress enter for quit")
    input()
    exit()
from system import *
P.init()
C=P.time.Clock()
RES=(320,200)
DISPLAY=P.display.set_mode(RES,depth=8,vsync=1)
FPS=60
CPU=0
DELTATIME=0
TICK=0
t=0
HUD=ObjectGroup()
BGO=ObjectGroup()
CON=[]
def controls():
    global CON
    i=P.key.get_pressed()
    CON=[i[P.K_RIGHT]-i[P.K_LEFT],i[P.K_DOWN]-i[P.K_UP],
    int(i[P.K_LCTRL]),int(i[P.K_LSHIFT]),int(i[P.K_z]),
    int(i[P.K_x]),int(i[P.K_c]),int(i[P.K_ESCAPE])]
def update():
    global TICK,color
    update_music()
    if(TICK>1):
        TICK-=1
        controls()
        HUD.update(CON,BGO,HUD)
        color=(0,0,0)
    HUD.draw(DISPLAY,TICK)
def display_reset(flag):
    global DISPLAY
    P.display.quit()
    DISPLAY=P.display.set_mode(RES,flag,depth=8,vsync=1)
def set_fps(i):
    global FPS
    FPS=i
from objects.menu import *
HUD.add(Menu())
while(1):
    color=(255,255,255)
    update()
    draw_text("FPS:"+str(round(C.get_fps())),(0,0),DISPLAY)
    draw_text("CPU:"+str(round(CPU*100)),(64,0),DISPLAY)
    draw_text("DT:"+str(DELTATIME)+"/50",(128,0),DISPLAY,color=color)
    draw_text("MUS:"+str(P.mixer.music.get_pos()/1000),(192,0),DISPLAY)
    draw_text(str(CON),(0,8),DISPLAY)
    P.mouse.set_visible(0)
    P.display.set_caption("RPG de física")
    for event in P.event.get():
        if event.type==P.QUIT:
            exit()
    P.display.flip()
    CPU=(P.time.get_ticks()-t)/(DELTATIME+1e-9)
    i=C.tick(FPS)
    DELTATIME=t
    t=P.time.get_ticks()
    DELTATIME=t-DELTATIME
    TICK+=DELTATIME/50
    DISPLAY.fill((0,0,255))
