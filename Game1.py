import pygame
import random

pygame.init()

game_width=800
game_height=600

gameWindow=pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption("Snake Game")

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

pygame.display.update()

block=20
FPS=10
clk=pygame.time.Clock()

font=pygame.font.SysFont("Arial",30,2)

def snake(block,snacklist):
    for XnY in snacklist:
        pygame.draw.rect(gameWindow,blue,[XnY[0],XnY[1],int(block),int(block)])

def msg_screen(msg,color):
    screen_text=font.render(msg,True,color)
    screen_text_1=font.render("Press ' r ' To Replay Or Press ' q ' To Quit",True,color)
    gameWindow.blit(screen_text,[int(game_width/2.5),int(game_height/3)])
    gameWindow.blit(screen_text_1,[int(game_width/6),int(game_height/2.5)])

background_image=pygame.image.load(r"D:\PFP\SahilPatel\Python App And Program\Snake Game\green2.jpg").convert()


def loop():
    start_x=game_width/2
    start_y=game_height/2
    update_x=0
    update_y=0
    gameClose=True
    gameOver=False

    rAppleX=round(random.randrange(50,750)/20.0)*20.0
    rAppleY=round(random.randrange(50,550)/20.0)*20.0

    snackList=[]
    snackLength=1

    while gameClose:
        while gameOver==True:
            gameWindow.fill(white)
            msg_screen("GAME OVER !",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameClose=False
                        gameOver=False
                    if event.key==pygame.K_r:
                        loop()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    update_x=-block
                    update_y=0

                if event.key==pygame.K_RIGHT:
                    update_x=block
                    update_y=0

                if event.key==pygame.K_UP:
                    update_y=-block
                    update_x=0

                if event.key==pygame.K_DOWN:
                    update_y=block
                    update_x=0

        if start_x >= game_width or start_x < 0 or start_y >= game_height or start_y < 0:
            gameOver=True

        start_x+=update_x
        start_y+=update_y
        gameWindow.blit(background_image,[0,0])
        pygame.draw.rect(gameWindow,red,[int(rAppleX),int(rAppleY),int(block),int(block)])
        # pygame.draw.rect(gameWindow,blue,[int(start_x),int(start_y),int(block),int(block)])

        snackHead=[]
        snackHead.append(start_x)
        snackHead.append(start_y)
        snackList.append(snackHead)

        if len(snackList)>snackLength:
            del(snackList[0])

        for eachSegment in snackList[:-1]:
            if eachSegment==snackHead:
                gameOver=True

        snake(block,snackList)

        pygame.display.update()

        if start_x==rAppleX and start_y==rAppleY:
            rAppleX=round(random.randrange(50,750)/20.0)*20.0
            rAppleY=round(random.randrange(50,550)/20.0)*20.0
            snackLength+=1
                       
        clk.tick(FPS)
    pygame.quit()

    quit()

loop()