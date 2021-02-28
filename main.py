import pygame
from pygame.locals import *
from my_errors import SpaceShipOutOffScreen

FPS = 60
WIN_WIDTH = 1300
WIN_HEIGHT = 800
BLACK = (0, 0, 0)
LIME = (180, 255, 100)
ORANGE = (255, 100, 10)
RED = (255, 0, 0)


class Ships(pygame.sprite.Sprite):  # класс для космических кораблей
    def __init__(self, x, y, file_name, team):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(file_name)
        self.team = team # атрибут определения кманды корабля
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw_ships(self): # общая функция отрисовки
        if self.team == "sh_l": # для левого корабля
            sc.blit(self.image, self.rect)
            if pygame.key.get_pressed()[K_LEFT]:
                self.rect.x -= 10
            if pygame.key.get_pressed()[K_RIGHT]:
                self.rect.x += 10
            if pygame.key.get_pressed()[K_UP]:
                self.rect.y -= 10
            if pygame.key.get_pressed()[K_DOWN]:
                self.rect.y += 10
            if self.rect.x > WIN_WIDTH + self.image.get_width() or self.x < 0 - self.image.get_width():  # создание исключений
                raise SpaceShipOutOffScreen("корабль за пределами поля в горизонтальной плоскости")
            elif self.rect.y > WIN_HEIGHT + self.image.get_height() or self.rect.y < 0 - self.image.get_height():
                raise SpaceShipOutOffScreen("корабль за пределами поля в вертикальной плоскости")

        if self.team == "sh_r":   # для правого корабля
            sc.blit(self.image, self.rect)
            if pygame.key.get_pressed()[K_a]:
                self.rect.x -= 10
            if pygame.key.get_pressed()[K_d]:
                self.rect.x += 10
            if pygame.key.get_pressed()[K_w]:
                self.rect.y -= 10
            if pygame.key.get_pressed()[K_s]:
                self.rect.y += 10
            if self.rect.x > WIN_WIDTH + self.image.get_width() or self.rect.x < 0 - self.image.get_width():  # создание исключений
                raise SpaceShipOutOffScreen("корабль за пределами поля в горизонтальной плоскости")
            elif self.rect.y > WIN_HEIGHT + self.image.get_height() or self.rect.y < 0 - self.image.get_height():
                raise SpaceShipOutOffScreen("корабль за пределами поля в вертикальной плоскости")


class Bullet():  # класс пуль
    def __init__(self, colour, radius, x, y, orient):
            self.colour = colour
            self.radius = radius
            self.x = x
            self.y = y
            self.orient = orient  # аргумент направления

    def bul_gun(self): # направление движения пуль
        if self.orient == "r":  #для координат правого корабля
            self.x += 5
        if self.orient == "l":   #для координат левого корабля
            self.x -= 5

    def draw_bul(self):
        pygame.draw.circle(sc, self.colour, (self.x, self.y), self.radius)

pygame.init()   # запуск игрового движка

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создание игрового окна

clock = pygame.time.Clock() # проверка заданой частоты

sh_l = Ships(WIN_WIDTH - 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\interprice.png', "sh_l")  # обьект левого корабля
sh_r = Ships(0 + 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\titanik.png', "sh_r")  # обьект правого корабля
arr = [] #  массив  для пуль левого орабля

while True: # запуск отрисовки
    sc.fill(BLACK)  # отрисовка окна
    clock.tick(FPS)  # частота обновления кадро

    sh_l.draw_ships()  # отрисовка левого
    sh_r.draw_ships()  # отрисовка пра


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