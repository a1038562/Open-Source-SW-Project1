import pygame as pg
from pygame import *
import sys
import time

pg.init() #모듈 초기화

clock=pg.time.Clock() #게임 루프 주기

d_width=1200 #가로
d_height=800 #세로
speed=10 #Player 이동속도
tick=30 

#초기 시작 위치
player_x=d_width/2
player_y=d_height/2-100

#이동 거리
move_x=0
move_y=0

#창 크기 설정
screen=pg.display.set_mode((d_width,d_height)) 

#게임 제목
pg.display.set_caption("Escape") 

#게임 이미지
backgroundIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\bgimg.PNG')
defaltIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\defaltimg.PNG')

Aevent2IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\aevent2.PNG')
Aevent3IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\aevent3.PNG')
Aevent4IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\aevent4.PNG')
Aevent5IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\aevent5.PNG')
Aevent6IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\aevent6.PNG')
Aevent8IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\aevent8.PNG')
Aevent10IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\aevent10.PNG')

titleIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\title.PNG')
startIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\startimg.PNG')
quitIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\quitimg.PNG')
startIMG2=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\startimg2.PNG')
quitIMG2=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\quitimg2.PNG')
gotitleIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\gotitleimg.PNG')
gotitleIMG2=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\gotitleimg2.PNG')
characterIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\charimg.PNG')
endIMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\endimg.PNG')

event1IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event1.PNG')
event2IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event2.PNG')
event3IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event3.PNG')
event4IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event4.PNG')
event5IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event5.PNG')
event6IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event6.PNG')
event7IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event7.PNG')
event8IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event8.PNG')
event9IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event9.PNG')
event10IMG=pg.image.load(r'C:\Users\Xenon\Desktop\escapegame\event10.PNG')


TAevent2IMG=pg.transform.scale(Aevent2IMG,(1200,1200))
TAevent3IMG=pg.transform.scale(Aevent3IMG,(1200,1200))
TAevent4IMG=pg.transform.scale(Aevent4IMG,(1200,1200))
TAevent5IMG=pg.transform.scale(Aevent5IMG,(1200,1200))
TAevent6IMG=pg.transform.scale(Aevent6IMG,(1200,1200))
TAevent8IMG=pg.transform.scale(Aevent8IMG,(1200,1200))
TAevent10IMG=pg.transform.scale(Aevent10IMG,(1200,1200))

TbackgroundIMG=pg.transform.scale(backgroundIMG,(1200,1200))
TstartIMG=pg.transform.scale(startIMG,(200,200)) 
TstartIMG2=pg.transform.scale(startIMG2,(200,200)) 
TquitIMG=pg.transform.scale(quitIMG,(200,200)) 
TquitIMG2=pg.transform.scale(quitIMG2,(200,200)) 
TquitIMGs=pg.transform.scale(quitIMG,(100,100)) 
TquitIMG2s=pg.transform.scale(quitIMG2,(100,100)) 
TgotitleIMGs=pg.transform.scale(gotitleIMG,(100,100))
TgotitleIMG2s=pg.transform.scale(gotitleIMG2,(100,100))
TtitleIMG=pg.transform.scale(titleIMG,(500,500))
TdefaltIMG=pg.transform.scale(defaltIMG,(1200,1200))
TcharacterIMG=pg.transform.scale(characterIMG,(72,136))

Tevent1IMG=pg.transform.scale(event1IMG,(542,163))
Tevent2IMG=pg.transform.scale(event2IMG,(542,163))
Tevent3IMG=pg.transform.scale(event3IMG,(542,163))
Tevent4IMG=pg.transform.scale(event4IMG,(542,163))
Tevent5IMG=pg.transform.scale(event5IMG,(542,163))
Tevent6IMG=pg.transform.scale(event6IMG,(542,163))
Tevent7IMG=pg.transform.scale(event7IMG,(542,163))
Tevent8IMG=pg.transform.scale(event8IMG,(542,163))
Tevent9IMG=pg.transform.scale(event9IMG,(542,163))
Tevent10IMG=pg.transform.scale(event10IMG,(542,163))

#버튼1
class Button:
    def __init__(self,before_img,x,y,IMGwidth,IMGheight,after_img,action=None):
        press=pg.mouse.get_pressed() #마우스 클릭 알기
        mouse=pg.mouse.get_pos() #마우스 위치 알기

        #마우스가 버튼 범위 내에서 클릭되었으면 버튼 이미지 변경 및 함수 실행
        if x<mouse[0]<x+IMGwidth and y<mouse[1]<y+IMGheight:
            screen.blit(before_img,(x,y))

            if press[0] and action !=None:
                screen.blit(after_img,(x,y))
                pg.display.update()
                time.sleep(0.5) #대기
                action()
        else:
            screen.blit(before_img,(x,y))

#버튼2
class Button2:
    def __init__(self,img,x,y,IMGwidth,IMGheight,action=None):
        press=pg.mouse.get_pressed()
        mouse=pg.mouse.get_pos()

        #마우스가 클릭되었으면 함수 실행
        if press[0]:
            pg.display.update()
            action()
             
        else:
            screen.blit(img,(x,y))
             
#Player 위치 설정
def location():
    global player_x,player_y

    player_x+=move_x
    player_y+=move_y

#Player가 화면 범위 안에 있도록 설정
    if player_x<50:
        player_x=50
    if player_y<50:
        player_y=50
    if player_x>1075:
         player_x=1075
    if player_y>575:
        player_y=575

#Player가 가구 위로 다닐 수 없도록 설정
#책상 위치
    if 50<player_x<200 and 150<player_y<400:
        player_x=200
    if 50<=player_x<=150 and 90<=player_y<=200:
        player_y=90
    if 50<=player_x<=150 and 200<=player_y<=450:
        player_y=450

#옷장 위치
    if 485<player_x<765 and 490<player_y:
        player_y=490

#책장 위치
    if 800<player_x and 470<player_y:
        player_y=470
    
#TV 위치
    if 920<player_x<970 and 170<player_y<420:
        player_x=920
    if 930<=player_x and 170<player_y<=300:
        player_y=170
    if 930<=player_x and 300<player_y<420:
        player_y=420

#게임 시작 시
def startGame():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): #이벤트 확인
            if event.type==pg.quit: #게임이 실행 중인지 확인 
                running=False

            #이동
            if event.type==pg.KEYDOWN:
                if event.key == ord('a'): #'a'를 누르면 왼쪽으로 이동
                    move_x-=speed
                if event.key == ord('d'): #'d'를 누르면 오른쪽으로 이동
                    move_x+=speed
                if event.key == ord('w'): #'w'를 누르면 위로 이동
                    move_y-=speed
                if event.key == ord('s'): #'s'를 누르면 아래로 이동
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #책상 이벤트
            if event.type==pg.KEYDOWN: #책상 앞에서 스페이스 바를 누르면 나이프 획득
                if player_x==200 and 150<player_y<400:
                    if event.key == ord(' '):
                       event1() #event1 실행

            screen.blit(TdefaltIMG,(0,-210)) #배경 이미지
            screen.blit(TcharacterIMG,(player_x,player_y)) #Player 이미지

            #타이틀로 돌아가기 버튼과 종료 버튼
            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location() #Player 위치

            clock.tick(tick) #게임 루프 주기

            pg.display.update() #화면 업데이트

##############################################################################################
            
def event1():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event1B=Button2(Tevent1IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent1) #버튼 클릭시 afterEvent1 실행
        pg.display.update()

def event2():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event2B=Button2(Tevent2IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent2)
        pg.display.update()

def event3():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event3B=Button2(Tevent3IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent3)
        pg.display.update()

def event4():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event4B=Button2(Tevent4IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent4)
        pg.display.update()

def event5():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event5B=Button2(Tevent5IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent5)
        pg.display.update()

def event6():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event6B=Button2(Tevent6IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent6)
        pg.display.update()

def event7():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event7B=Button2(Tevent7IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent7)
        pg.display.update()

def event8():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event8B=Button2(Tevent8IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent8)
        pg.display.update()

def event9():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event9B=Button2(Tevent9IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent9)
        pg.display.update()

def event10():
    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:  
                running=False
            
        event10B=Button2(Tevent10IMG,d_width/2-271,d_height*4/5-80,542,163,afterEvent10)
        pg.display.update()
##############################################################################################
def afterEvent1():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0   

            #왼쪽 그림 이벤트
            if event.type==pg.KEYDOWN: #왼쪽 그림 앞에서 스페이스 바를 누르면 성냥개비 획득
                if 100<=player_x<=200 and player_y==50:
                    if event.key == ord(' '):
                        event2()

            screen.blit(TdefaltIMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent2():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #종이 이벤트
            if event.type==pg.KEYDOWN: #종이 앞에서 스페이스 바를 누르면 컴퓨터 암호 획득
                if player_x==200 and 275<player_y<400:
                    if event.key == ord(' '):
                        event3()

            screen.blit(TAevent2IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent3():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #컴퓨터 이벤트
            if event.type==pg.KEYDOWN: #컴퓨터 앞에서 스페이스 바를 누르면 옷장을 여는 힌트 획득
                if player_x==200 and 150<player_y<275:
                    if event.key == ord(' '):
                        event4()

            screen.blit(TAevent3IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent4():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #옷장 이벤트
            if event.type==pg.KEYDOWN: #옷장 앞에서 스페이스 바를 누르면 집게전선 획득
                if 485<player_x<765 and player_y==490:
                    if event.key == ord(' '):
                        event5()
        
            screen.blit(TAevent4IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent5():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #전선 이벤트
            if event.type==pg.KEYDOWN: #빨간 전선을 연결하면 TV 켜짐
                if player_x==1075 and 50<player_y<150:
                    if event.key == ord(' '):
                        event6()
        
            screen.blit(TAevent5IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent6():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #TV 이벤트
            if event.type==pg.KEYDOWN: #TV 화면을 보면 시계 힌트 획득
                if player_x==920 and 170<player_y<420:
                    if event.key == ord(' '):
                        event7()
        
            screen.blit(TAevent6IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent7():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #TV 이벤트
            if event.type==pg.KEYDOWN: #시곗바늘을 돌려서 액자 움직이기
                if 100<player_x<250 and player_y==575:
                    if event.key == ord(' '):
                        event8()
        
            screen.blit(TAevent6IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent8():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #액자2 이벤트
            if event.type==pg.KEYDOWN: #액자2 자리에서 드라이버 획득
                if 300<=player_x<=400 and player_y==50:
                    if event.key == ord(' '):
                        event9()
        
            screen.blit(TAevent8IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent9():
    global player_x,player_y,move_x,move_y

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False

            if event.type==pg.KEYDOWN:
                if event.key == ord('a'):
                    move_x-=speed
                if event.key == ord('d'):
                    move_x+=speed
                if event.key == ord('w'):
                    move_y-=speed
                if event.key == ord('s'):
                    move_y+=speed
            if event.type==pg.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    move_x=0
                elif event.key == ord('w') or event.key == ord('s'):
                    move_y=0  

            #환기구
            if event.type==pg.KEYDOWN: #드라이버로 환기구 커버를 열고 탈출
                if 660<=player_x<=740 and player_y==50:
                    if event.key == ord(' '):
                        event10()
        
            screen.blit(TAevent8IMG,(0,-210))
            screen.blit(TcharacterIMG,(player_x,player_y))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()

def afterEvent10():
    #게임 종료 화면

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit: 
                running=False 

            screen.blit(TAevent10IMG,(0,-210))
            screen.blit(endIMG,(0,250))

            gotitleB=Button(TgotitleIMGs,d_width*8/10-30,d_height*9/10,100,100,TgotitleIMG2s,main)
            quitB2=Button(TquitIMGs,d_width*9/10-30,d_height*9/10,100,100,TquitIMG2s,quit)
            
            location()

            clock.tick(tick)

            pg.display.update()
##############################################################################################

#종료           
def quit():
    pg.quit()
    sys.exit()

#게임 타이틀 화면
def main():
    global player_x,player_y

    player_x=d_width/2
    player_y=d_height/2-100

    running=True

    while running:
        for event in pg.event.get(): 
            if event.type==pg.quit:
                quit()

            screen.blit(TbackgroundIMG,(0,-210)) #배경 이미지
            screen.blit(TtitleIMG,(d_width/2-260,d_height/2-300)) #타이틀 이미지

            #게임 스타트 버튼과 종료 버튼
            startB=Button(TstartIMG,d_width*1/2-350,d_height*2/3,200,200,TstartIMG2,startGame)
            quitB=Button(TquitIMG,d_width*1/2+150,d_height*2/3,200,200,TquitIMG2,quit)
            pg.display.update()
         

main()