import pygame
from pygame.locals import *
from my_errors import MyError

FPS = 60
WIN_WIDTH = 1300
WIN_HEIGHT = 800
BLACK = (0, 0, 0)
LIME = (180, 255, 100)
ORANGE = (255, 100, 10)
RED = (255, 0, 0)

class Ships(pygame.sprite.Sprite):  # родительски класс для космических кораблей
    def __init__(self, x, y, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(file_name)


class Ships_left(Ships):  # класс для корабля левого
    def __init__(self,x, y,  file_name, ):
        super().__init__(x, y,  file_name)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw_left(self):
        sc.blit(self.image, self.rect)
        if pygame.key.get_pressed()[K_LEFT]:
            self.rect.x -= 10
        if pygame.key.get_pressed()[K_RIGHT]:
            self.rect.x += 10
        if pygame.key.get_pressed()[K_UP]:
            self.rect.y -= 10
        if pygame.key.get_pressed()[K_DOWN]:
            self.rect.y += 10
        """if self.x > WIN_WIDTH + self.radius or self.x < 0 - self.radius:
            raise MyError("корабль за пределами поля в горизонтальной плоскости")
        elif self.y > WIN_HEIGHT + self.radius or self.y < 0 - self.radius:
            raise MyError("корабль за пределами поля в вертикальной плоскости")"""

class Ships_right(Ships):  # класс корабля правого
    def __init__(self,x, y,  file_name):
        super().__init__(x, y,  file_name)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw_right(self):
        sc.blit(self.image, self.rect)
        if pygame.key.get_pressed()[K_a]:
            self.rect.x -= 10
        if pygame.key.get_pressed()[K_d]:
            self.rect.x += 10
        if pygame.key.get_pressed()[K_w]:
            self.rect.y -= 10
        if pygame.key.get_pressed()[K_s]:
            self.rect.y += 10
        """if self.x > WIN_WIDTH + self.rect.x or self.rect.x < 0 - self.rect:
            raise MyError("корабль за пределами поля в горизонтальной плоскости")
        elif self.y > WIN_HEIGHT + self.rect or self.y < 0 - self.rect:
            raise MyError("корабль за пределами поля в вертикальной плоскости")"""


class Bullet():  # класс пуль
    def __init__(self, colour, radius, x, y, orient):
            self.colour = colour
            self.radius = radius
            self.x = x
            self.y = y
            self.orient = orient  # аргумент направления

    def bul_gun(self): # направление движения пуль
        if self.orient == "r": #для координат правого корабля
            self.x += 5
        if self.orient == "l":  #для координат левого корабля
            self.x -= 5

    def draw_bul(self):
        pygame.draw.circle(sc, self.colour, (self.x, self.y), self.radius)

pygame.init()   # запуск игрового движка

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создание игрового окна

clock = pygame.time.Clock() # проверка заданой частоты

sh_l = Ships_left(WIN_WIDTH - 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\interprice.png')  # обьект левого корабля
sh_r = Ships_right(0 + 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\titanik.png')  # обьект правого корабля
arr = [] #  массив  для пуль левого орабля

while True: # запуск отрисовки
    sc.fill(BLACK)  # отрисовка окна
    clock.tick(FPS)  # частота обновления кадро

    sh_l.draw_left()  # отрисовка левого
    sh_r.draw_right() # отрисовка пра



    for i in pygame.event.get():  # запись действий за цикл
        if i.type == pygame.QUIT:  # если нажата кнопка выхода, выйти
            exit()
        if i.type == pygame.KEYUP: # фиксация нажтия
            if i.key == pygame.K_q: #  создание обькта пули правого корабля и загрузка его в массив
                gun = Bullet(RED, 20, sh_r.rect.x, sh_r.rect.y, "r")
                arr.append(gun)

            if i.key == pygame.K_BACKSPACE:  #  создание обькта пули левого корабля и загрузка его в массив
                gun = Bullet(RED, 20, sh_l.rect.x, sh_l.rect.y, "l")
                arr.append(gun)

    for gun in arr:  #  отрисовка пуль правого корабля и удадение из масива обьктов за пределами экрана
        gun.draw_bul()
        gun.bul_gun()
        if gun.x >= WIN_WIDTH + gun.radius or gun.x <= 0 - gun.radius:
            arr.remove(gun)

    pygame.display.update()   #  обновление экрана