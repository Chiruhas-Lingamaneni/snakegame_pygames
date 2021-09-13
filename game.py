import pygame
from pygame.math import Vector2
from random import randint
pygame.init()

class Snake():
    def __init__(self):
        self.body=[Vector2(4,3),Vector2(3,3),Vector2(2,3)]
        self.xx=1
        self.yy=0
        self.increase=False
    def sbody(self):
        head=True
        for each in self.body:
            
            self.food_square=pygame.Rect(int(each.x*25),int(each.y*25),25,25)
            if head==True:
                pygame.draw.rect(screen,(255,0,0),self.food_square)
                head=False
            else:
                pygame.draw.rect(screen,(0,0,255),self.food_square)
    def move(self):
        if self.increase==False:
            tempv=self.body[0:-1]
        elif self.increase==True:
            tempv=self.body[:]
            self.increase=False
        self.body=[tempv[0]+Vector2(self.xx,self.yy)]+tempv

class Food():
    def __init__(self):
        self.food=Vector2(randint(0,grids-1),randint(0,grids-1))
    def position(self):
                
        self.food_square=pygame.Rect(self.food.x*25,self.food.y*25,25,25)   
        pygame.draw.circle(screen,(255,223,0),(self.food.x*25+25/2,self.food.y*25+25/2),box/2)

class Main():
    def __init__(self):
        self.food=Food()
        self.snake=Snake()
    def play(self):
        self.background()
        self.food.position()
        self.snake.sbody()
        for event in pygame.event.get():
            global running
            if event.type==pygame.QUIT:
                running=False
            if event.type==screen_update:
                self.snake.move()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if self.snake.xx !=1:
                        self.snake.xx,self.snake.yy=-1,0
                if event.key==pygame.K_RIGHT:
                    if self.snake.xx !=-1:
                        self.snake.xx,self.snake.yy=1,0
                if event.key==pygame.K_UP:
                    if self.snake.yy !=1:
                        self.snake.xx,self.snake.yy=0,-1
                if event.key==pygame.K_DOWN:
                    if self.snake.yy !=-1:
                        self.snake.xx,self.snake.yy=0,1
        self.eat()
        self.collide()
        self.score()
    def background(self):
        darkgreen=(34,139,34)
        litegreen=(0,128,0)
        for y in range(grids):
            if y%2==0:
                for x in range(grids):
                    cube=pygame.Rect(x*25,y*25,25,25)
                    if x%2==0:       
                        pygame.draw.rect(screen,darkgreen,cube)
                    else:
                        pygame.draw.rect(screen,litegreen,cube)
            else:
                for x in range(grids):
                    cube=pygame.Rect(x*25,y*25,25,25)
                    if x%2==1:       
                        pygame.draw.rect(screen,darkgreen,cube)
                    else:
                        pygame.draw.rect(screen,litegreen,cube)
    def score(self):
        myscore=len(self.snake.body)-3
        scorefont=font.render(str(myscore),True,((0,0,0)))
        screen.blit(scorefont,(box*grids-30,20))
    def eat(self):
        if self.snake.body[0]==self.food.food:
            self.food=Food()
            for body in self.snake.body:
                if body.x==self.food.food.x and body.y==self.food.food.y:
                    self.food=Food() 
            self.snake.increase=True
    def collide(self):
        if not(0<=self.snake.body[0].x<grids) or not(0<=self.snake.body[0].y<grids):
            self.gameover()
        for part in self.snake.body[1:]:
            if self.snake.body[0]==part:
                self.gameover()
    def gameover(self):
        self.snake.body=[Vector2(4,3),Vector2(3,3),Vector2(2,3)]
        self.snake.xx=0
        self.snake.yy=0

if __name__ == '__main__':

    box=25
    grids=25
    screen = pygame.display.set_mode((box*grids,box*grids))
    clock=pygame.time.Clock()
    screen_update=pygame.USEREVENT
    pygame.time.set_timer(screen_update,150)
    running=True
    font=pygame.font.Font(None,25)
    pygame.display.set_caption("Snake game")

    main=Main()
    while running:
        screen.fill((255,255,0))
        main.play()
        pygame.display.update()
        clock.tick(60)