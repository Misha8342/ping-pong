from pygame import *
from random import randint
import time as tomers  

font.init()
font1 = font.Font(None, 80)
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed1, speed_player2):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed1


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.speed2 = speed_player2
 #метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_tarelka1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 380:
            self.rect.y += self.speed
    def update_tarelka2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 380:
            self.rect.y += self.speed

class Bol(GameSprite):
    def update_bol(self):
        self.rect.x += self.speed
        global bol_x
        bol_x += self.speed
        self.rect.y += self.speed2
        if self.rect.y >= 440 or self.rect.y <= 0:
            self.speed2 = self.speed2*-1
        if sprite.collide_rect(tarelka1,bol) or sprite.collide_rect(tarelka2,bol):
            self.speed = self.speed*-1

#self.rect.x >= 700 or self.rect.x <= 0 or 
#if self.rect.y <= 0 or self.rect.x <= 0 or sprite.collide_rect(tarelka1,bol) or sprite.collide_rect(tarelka2,bol):
#self.speed_player2 = self.speed_player2*-1
#sprite.groupcollide(shp2,shp1,False,False)
#создаем окошко
win_width = 700
win_height = 500
backgrod = 'galaxy.jpg'
mach = 'asteroid.png'
platform1 = 'ufo1.png'
platform2 = 'ufo2.png'
display.set_caption("ping-pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(backgrod), (win_width, win_height))

tarelka1 = Player(platform1, 50, 200, 70, 120, 5,0)
tarelka2 = Player(platform2, 550, 200, 70, 120, 5,0)

tarelks = sprite.Group()
tarelks.add(tarelka1)
tarelks.add(tarelka2)

bol_x = 310
bol_y = 220
bol = Bol(mach, bol_x, bol_y, 60, 60, 5,5)

bols = sprite.Group()
bols.add(bol)

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
clock = time.Clock() 
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
    clock.tick(15)
    #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        #обновляем фон
        window.blit(background,(0,0))

        if bol_x < 30 or bol_x > 570:
            window.blit(lose,(10,70))
            finish = True
        bol.update_bol()
        tarelka1.update_tarelka1()
        tarelka2.update_tarelka2()

        bol.reset()
        tarelka1.reset()
        tarelka2.reset()

    display.update()