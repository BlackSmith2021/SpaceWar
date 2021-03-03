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

    def update(self): # общая функция отрисовки
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


class Bullet(pygame.sprite.Sprite):  # класс пуль
    def __init__(self, x, y, orient):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(LIME)
        self.x = x
        self.y = y
        self.orient = orient  # аргумент направления
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        sc.blit(self.image, self.rect)
        if self.orient == "r":  #для координат правого корабля
            self.rect.x += 5
            if self.rect.left > WIN_WIDTH:
                self.kill()
        if self.orient == "l":   #для координат левого корабля
            self.rect.x -= 5
            if self.rect.right < 0:
                self.kill()

pygame.init()   # запуск игрового движка

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создание игрового окна

clock = pygame.time.Clock() # проверка заданой частоты
all_sprites = pygame.sprite.Group()  # создание группы для спрайтов

sh_l = Ships(WIN_WIDTH - 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\interprice.png', "sh_l")  # обьект левого корабля
sh_r = Ships(0 + 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\titanik.png', "sh_r")  # обьект правого корабля
all_sprites.add(sh_r, sh_l)  # добавление обьектов спрайтов в группу
bul_sprites = pygame.sprite.Group()

while True: # запуск отрисовки
    sc.fill(BLACK)  # отрисовка окна
    clock.tick(FPS)  # частота обновления кадро

    all_sprites.update()  # отрисовка группы спрайтов
    bul_sprites.update()

    for i in pygame.event.get():  # запись действий за цикл
        if i.type == pygame.QUIT:  # если нажата кнопка выхода, выйти
            exit()
        if i.type == pygame.KEYUP:  # фиксация нажтия
            if i.key == pygame.K_q:  #  создание обькта пули правого корабля и загрузка его в массив
                gun = Bullet(sh_r.rect.x, sh_r.rect.y, "r")
                bul_sprites.add(gun)

            if i.key == pygame.K_BACKSPACE:  #  создание обькта пули левого корабля и загрузка его в массив
                gun = Bullet(sh_l.rect.x, sh_l.rect.y, "l")
                bul_sprites.add(gun)

    pygame.display.update()   #  обновление экрана