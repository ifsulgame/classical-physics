import pygame as P
from system import *
from __main__ import display_reset
from __main__ import set_fps
class Menu:
    def __init__(self):
        self.stat=0
        self.menu=0
        self.select=0
        self.button=0
        self.pos=512
        self.Ppos=512
    def menu_sys(self,opt,CON):
        if(self.button==int(self.button)):
            self.select=clamp(self.select+CON[1],0,opt)
            if(CON[4]==1):
                return 1
            elif(self.menu==0 and CON[5]==1):
                self.select=opt
                return 1
        i=(CON[1]!=0)+CON[4]+CON[5]
        self.button=clamp(self.button+i/8,0,1)
        if(i==0):
            self.button=0
        return 0
    def fade_in(self):
        self.pos=int(self.pos-self.pos/4)
        if(self.pos==0):
            self.stat=1
    def fade_off(self):
        self.pos=int(self.pos+self.pos+1)
        if(self.pos>512):
            return 1
        return 0
    def update(self,CON,BGO,HUD):
        global DISPLAY,FPS
        self.Ppos=self.pos
        if(self.stat==0):
            self.fade_in()
        elif(self.stat==1):
            if(self.menu==1 or self.menu==2):
                i=4
            else:
                i=3
            i=self.menu_sys(i,CON)
            if(i==1):
                if(self.menu==1 and self.select<3):
                    if(self.button==0):
                        if(self.select==0):
                            display_reset(0)
                        elif(self.select==1):
                            display_reset(P.FULLSCREEN)
                        elif(self.select==2):
                            display_reset(P.SCALED|P.FULLSCREEN)
                elif(self.menu==2 and self.select<4):
                    if(self.button==0):
                        if(self.select==0):
                            set_fps(60)
                        elif(self.select==1):
                            set_fps(120)
                        elif(self.select==2):
                            set_fps(240)
                        elif(self.select==3):
                            set_fps(9999)
                else:
                    self.stat=2
        else:
            i=self.fade_off()
            if(i==1):
                if(self.menu==0):
                    if(self.select==1):
                        HUD.add(MusicRoom())
                        HUD.kill(self)
                    elif(self.select==2):
                        self.menu=1
                    elif(self.select==3):
                        exit()
                elif(self.menu==1):
                    if(self.select==3):
                        self.menu=2
                    elif(self.select==4):
                        self.menu=0
                elif(self.menu==2):
                    if(self.select==4):
                        self.menu=1
                self.stat=0
                self.select=0
                self.button=0
                self.pos=512
    def draw(self,DISPLAY,TICK):
        pos=self.Ppos+(self.pos-self.Ppos)*TICK
        if(self.menu==0):
            i=(self.select==0)*155+100
            draw_text("Play",(160-pos,80),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==1)*155+100
            draw_text("Music Room",(160+pos,100),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==2)*155+100
            draw_text("Config",(160-pos,120),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==3)*155+100
            draw_text("Exit",(160+pos,140),DISPLAY,align=1,font=1,color=(i,i,i))
        elif(self.menu==1):
            i=(self.select==0)*155+100
            draw_text("Window",(160-pos,80-pos),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==1)*155+100
            draw_text("FullScreen",(160+pos,100-pos),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==2)*155+100
            draw_text("Borderless",(160-pos,120+pos),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==3)*155+100
            draw_text("Frame Rate",(160+pos,140+pos),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==4)*155+100
            draw_text("Back",(160-pos,160-pos),DISPLAY,align=1,font=1,color=(i,i,i))
        elif(self.menu==2):
            i=(self.select==0)*155+100
            draw_text("60 FPS",(160,80-pos),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==1)*155+100
            draw_text("120 FPS",(160,100-pos*1.2),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==2)*155+100
            draw_text("240 FPS",(160,120-pos*1.4),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==3)*155+100
            draw_text("No limit",(160,140-pos*1.8),DISPLAY,align=1,font=1,color=(i,i,i))
            i=(self.select==4)*155+100
            draw_text("Back",(160,160-pos*2),DISPLAY,align=1,font=1,color=(i,i,i))
class MusicRoom:
    def __init__(self):
        self.stat=0
        self.select=0
        self.button=0
        self.pos=512
        self.Ppos=512
    def menu_sys(self,opt,CON):
        if(self.button==int(self.button)):
            self.select=clamp(self.select+CON[1],0,opt)
            if(CON[4]==1):
                return 1
            elif(CON[5]==1):
                return 2
        i=(CON[1]!=0)+CON[4]+CON[5]
        self.button=clamp(self.button+i/8,0,1)
        if(i==0):
            self.button=0
        return 0
    def fade_in(self):
        self.pos=int(self.pos-self.pos/4)
        if(self.pos==0):
            self.stat=1
    def fade_off(self):
        self.pos=int(self.pos+self.pos+1)
        if(self.pos>512):
            return 1
        return 0
    def update(self,CON,BGO,HUD):
        self.Ppos=self.pos
        if(self.stat==0):
            self.fade_in()
        elif(self.stat==1):
            i=self.menu_sys(3,CON)
            if(i==1):
                if(self.select==0):
                    music_play("Cirno Stage")
                elif(self.select==1):
                    music_play("Shanghai!!!")
                elif(self.select==2):
                    music_play("Brutal Sister")
                elif(self.select==3):
                    music_play("Sis")
            elif(i==2):
                self.stat=2
        else:
            i=self.fade_off()
            if(i==1):
                HUD.add(Menu())
                HUD.kill(self)
    def draw(self,DISPLAY,TICK):
        pos=self.Ppos+(self.pos-self.Ppos)*TICK
        draw_text("Music Room",(32-pos,32),DISPLAY,font=1,color=(0,127,255),mode=3)
        i=(self.select==0)*155+100
        draw_text("Cirno Stage",(32,64-pos),DISPLAY,color=(i,i,i))
        i=(self.select==1)*155+100
        draw_text("Shanghai!!!",(32,72-pos),DISPLAY,color=(i,i,i))
        i=(self.select==2)*155+100
        draw_text("Brutal Sister",(32,80-pos),DISPLAY,color=(i,i,i))
