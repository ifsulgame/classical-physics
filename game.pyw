import subprocess as SUB
import sys
try:
    import pygame as P
except:
    try:
        sys.path.append("__package\site-packages")
        #print(sys.path)
    except:
        print("Start")
        SUB.check_call([sys.executable, "-m", "pip", "install", 'pygame'])
        print("Finish")
finally:
    import pygame as P
from system import *
P.init()
C=P.time.Clock()
DISPLAY=P.Surface((320,240),depth=12)
LINESURF=P.Surface((640,480),depth=8)
i=85
LINESURF.fill((i,i,i))
SCALESURF=P.Surface((640,240),depth=12)
for i in range(320):
    P.draw.line(LINESURF,(0,0,0),(0,1+i*2),(640,1+i*2))
FPS=60
CPU=0
DELTATIME=0
TICK=0
t=0
HUD=ObjectGroup()
BGO=ObjectGroup()
CON=[]
JOYID={}
def get_joystick_id():
    return JOYID
def controls():
    global CON
    i=P.key.get_pressed()
    CON=[i[P.K_RIGHT]-i[P.K_LEFT],i[P.K_DOWN]-i[P.K_UP],
    int(i[P.K_LCTRL]),int(i[P.K_LSHIFT]),int(i[P.K_z]),
    int(i[P.K_x]),int(i[P.K_c]),int(i[P.K_ESCAPE])]
    for j in JOYID.values():
        if(j.get_numaxes()>5):
            i=j.get_hat(0)
            CON[0]+=i[0]
            CON[1]-=i[1]
            i=j.get_axis(0)
            CON[0]+=(i>0.3)-(i<-0.3)
            i=j.get_axis(1)
            CON[1]+=(i>0.3)-(i<-0.3)
            i=j.get_axis(4)
            CON[2]+=(i>0.3)
            i=j.get_axis(5)
            CON[3]+=(i>0.3)
            i=get_joystick()
            CON[4]+=j.get_button(i[0])
            CON[5]+=j.get_button(i[1])
            CON[6]+=j.get_button(i[2])
            CON[7]+=j.get_button(i[3])
def update():
    global TICK,color
    if(TICK>1):
        TICK-=1
        controls()
        HUD.update(CON,BGO,HUD)
        color=(0,0,0)
    HUD.draw(DISPLAY,TICK)
def display_reset(flag):
    global DISPLAY,LINESURF,SCALESURF,SCREEN,SCALINESS
    SCALINESS=0
    P.display.quit()
    SCREEN=P.display.set_mode((640,480),flag,vsync=1)
    if(flag==P.FULLSCREEN):
        SCALINESS=1
    DISPLAY=DISPLAY.convert()
    LINESURF=LINESURF.convert()
    #SCALESURF=SCALESURF.convert()
def set_fps(i):
    global FPS
    FPS=i
display_reset(0)
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
        if event.type==P.JOYDEVICEADDED:
            joy=P.joystick.Joystick(event.device_index)
            JOYID[joy.get_instance_id()]=joy
            print(f"Joystick {joy.get_instance_id()} connected")
        if event.type==P.JOYDEVICEREMOVED:
            del JOYID[event.instance_id]
            print(f"Joystick {event.instance_id} disconnected")
    if(SCALINESS==0):
        #rescale
        SCALESURF.blit(P.transform.scale(DISPLAY,(640,240)),(0,0))
        SCREEN.blit(P.transform.scale(SCALESURF,(640,480)),(0,0))
    elif(SCALINESS==1):
        #scaliness
        SCALESURF.blit(P.transform.smoothscale(DISPLAY,(640,240)),(0,0))
        SCREEN.blit(P.transform.scale(SCALESURF,(640,480)),(0,0))
        SCREEN.blit(LINESURF,(0,0),special_flags=P.BLEND_SUB)
    P.display.flip()
    CPU=(P.time.get_ticks()-t)/(DELTATIME+1e-9)
    C.tick(FPS)
    DELTATIME=t
    t=P.time.get_ticks()
    DELTATIME=t-DELTATIME
    TICK+=DELTATIME/50
    DISPLAY.fill((0,0,255))
