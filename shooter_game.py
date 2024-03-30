#Создай собственный Шутер!
from pygame import *
from random import randint
#mixer.init()
init()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
shoot=mixer.Sound('fire.ogg')

display.set_caption('???')
linox=display.set_mode((700,500))
bg=transform.scale(image.load('galaxy.jpg'),(700,500))
#создай окно игры
class Chvk(sprite.Sprite):
    def __init__(self,png,x,y,h,w):
        super().__init__()
        self.png=transform.scale(image.load(png),(h,w))
        self.rect=self.png.get_rect()
        self.rect.x=x
        self.rect.y=y
    def drawd(self):
        linox.blit(self.png,(self.rect.x,self.rect.y))
class Pl(Chvk):
    def __init__(self,png,x,y,h,w):
        super().__init__(png,x,y,h,w)
        self.game_con=1
    def update(self,key_p):
        if key_p[K_a]and self.rect.x>0 and self.game_con==1:
            self.rect.x-=5
        if key_p[K_d]and self.rect.x+50<700 and self.game_con==1:
            self.rect.x+=5
class En(Chvk):
    def __init__(self,png,x,y,h,w,pl_speed):
        super().__init__(png,x,y,h,w)
        self.pl_speed=pl_speed
        self.move_r=False
        self.move_l=False
    def update(self):
        if self.move_l==True:
            pl2.rect.x-=5
        if self.move_r==True:
            self.rect.x+=5
        if self.rect.x+25>=675:
            self.move_l=True
            self.move_r=False
        if pl2.rect.x<=500:
            self.move_l=False
            self.move_r=True
class Bullet(sprite.Sprite):
    def __init__(self,bul,damage,x_b, y_b, width_b, heigth_b):
        super().__init__()
        self.bal=transform.scale(image.load(bul),(10,30))
        self.damage=damage
        self.rect=Rect(x_b, y_b+10, width_b, heigth_b)
        self.coor_x=x_b
        self.coor_y=y_b
        self.bull=0
    def draw_fire(self):
        linox.blit(self.bal,(self.coor_x,self.coor_y))
    def draw_fire_2(self):
        linox.blit(self.bal,(self.rect.x,self.rect.y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Card():
    def __init__(self,x,y,width,heigth):
        self.rect=Rect(x, y, width, heigth)
    def set_text(self,text,size):
        self.image=font.Font(None,size).render(str(text),True,(255,0,0))
    def draw_text(self):
        linox.blit(self.image,(self.rect.x,self.rect.y))

defeat=Card(-200,250,0,0)
reset=Card(-200,300,0,0)
win=Card(-200,250,0,0)
pl=Pl('rocket.png',100,400,50,50)
prop=0
nadpis=Card(250,5,0,0)
nadpis.set_text(0,30)
score=Card(200,5,0,0)
score.set_text('Счёт:',30)
def_1=Card(320,25,0,0)
def_1.set_text(prop,30)
def_2=Card(200,25,0,0)
def_2.set_text('Пропущено:',30)
bullets=30
bullets_score=Card(200,55,0,0)
bullets_score.set_text('Патроны:',30)
bullets_score2=Card(320,55,0,0)
bullets_score2.set_text(bullets,30)

game_con=1
freeze=Card(200,100,0,0)
freeze.set_text('freeze',30)
boost=Card(320,100,0,0)
boost.set_text('boost for HP',30)


Hp=100
HP=Card(20,55,0,0)
HP.set_text('HP:',30)
HP2=Card(50,55,0,0)
HP2.set_text(HP,30)
#pl3=Chvk('treasure.png',600,450,50,50,col,col)
run=True
clock=time.Clock()
FPS=30
pov=0
povtorenye=0
fru=0
rect=Rect(100, 100, 100, 100)
key_p=key.get_pressed()
enemys=[]
asteroids_book=[]
for pl2 in range(5):
    pl2=En('ufo.png',randint(0,600),0,100,50,randint(1,2))
    enemys.append(pl2)
for aste in range(2):
    aste=En('asteroid.png',randint(0,600),0,75,75,randint(1,2))
    asteroids_book.append(aste)
bullets_book=[]
points=0
loose=0
while run:
    display.update()
    key_p=key.get_pressed()
    linox.blit(bg,(0,0))
    pl.drawd()
    #pl3.drawd()
    #linox.blit(rect,(100,100))
    for e in event.get():
        if e.type==QUIT:
            quit()
            run=False
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            x,y=e.pos
            if x>=boost.rect.x and x<=boost.rect.x+150 and y>=boost.rect.y and y<=boost.rect.y+30:
                povtorenye=3
                pov=30#🤣
            if x>=freeze.rect.x and x<=freeze.rect.x+150 and y>=freeze.rect.y and y<=freeze.rect.y+30:
                fru=100
        if e.type==MOUSEBUTTONDOWN and e.button==1 and pl.game_con==1 and bullets>0:
            x,y=e.pos
            bullett=Bullet('bullet.png',25,pl.rect.x+15,pl.rect.y-5,25,10)
            bullett.draw_fire_2()
            bullett.bull=190
            bullets_book.append(bullett)
            shoot.play()
            bullets-=1
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            x,y=e.pos
            if x>=reset.rect.x and x<=reset.rect.x+150 and y>=reset.rect.y and y<=reset.rect.y+30:
                pl.rect.x=100
                pl.rect.y=400
                pl.game_con=1
                game_con=1
                points=0
                for pl2 in enemys:
                    pl2.rect.y=0
                    pl2.rect.x=randint(0,600)
                for aste in asteroids_book:
                    aste.rect.x=randint(0,600)
                    aste.rect.y=0
                win.rect.x=-200
                reset.rect.x=-200
                prop=0
                defeat.rect.x=-200
                bullets=30
                Hp=100
                loose=0
    for pl2 in enemys:
        if game_con==1 and loose==0:
            pl2.rect.y+=pl2.pl_speed
        pl2.drawd()
        for aste in asteroids_book:
            if game_con==1 and loose==0:
                aste.rect.y+=pl2.pl_speed
            aste.drawd()
            if aste.rect.y>=425:
                aste.rect.x=randint(0,600)
                aste.rect.y=0
            if pl2.rect.y>=425 and pl.game_con==1:
                pl2.rect.x=randint(0,600)
                pl2.rect.y=0
                prop+=1
            if Hp<=0 or prop>=5:
                loose=1
                defeat.rect.x=200
                defeat.set_text('YOU LOSE!!! HAHA',35)
                defeat.draw_text()
                pl.game_con=0
                game_con=0
                reset.rect.x=200
                reset.set_text('играть заново',20)
                reset.draw_text()
            if sprite.collide_rect(pl,pl2) and pl.game_con==1:
                Hp-=25
                pl2.rect.y=0
                pl2.rect.x=randint(0,600)
            if sprite.collide_rect(pl,aste) and pl.game_con==1:
                Hp-=25
                aste.rect.y=0
                aste.rect.x=randint(0,600)
            for bb in bullets_book:
                if sprite.collide_rect(bb,pl2):
                    pl2.rect.y=0
                    pl2.rect.x=randint(0,600)
                    points+=1
                    bb.rect.x=-8000
                    bullets_book.remove(bb)
                if sprite.collide_rect(bb,aste):
                    aste.rect.y=0
                    aste.rect.x=randint(0,600)
                    bb.rect.x=-8000
                    bullets_book.remove(bb)
                bb.rect.y-=3
                bb.bull-=1
                if bb.bull<=0:
                    bullets_book.remove(bb)
                bb.draw_fire_2()
    if points>=10:
        loose=1
        win.set_text('YOU WIN!!!',50)
        win.draw_text()
        win.rect.x=200
        reset.rect.x=200
        reset.set_text('играть заново',20)
        reset.draw_text()
        pl.game_con=0
    
    if pov>0:
        pov-=1
    if pov<=0 and povtorenye>0:
        Hp+=25
        pov=30
        povtorenye-=1
    if Hp>100:
        Hp=100
    
    if fru>0:
        fru-=1
        game_con=0
    if fru<=0 and loose==0:
        game_con=1
    #if loose==1:
    #    game_con=0
    
    bullets_score.set_text('Патроны:',30)
    bullets_score.draw_text()
    bullets_score2.set_text(bullets,30)
    bullets_score2.draw_text()
    HP.draw_text()
    HP2.set_text(Hp,30)
    HP2.draw_text()

    freeze.draw_text()
    boost.draw_text()
    
    nadpis.set_text(points,30)
    nadpis.draw_text()
    score.set_text('Счёт:',30)
    score.draw_text()
    def_1.set_text(prop,30)
    def_1.draw_text()
    def_2.set_text('Пропущено:',30)
    def_2.draw_text()

    pl.update(key_p)
    clock.tick(FPS)