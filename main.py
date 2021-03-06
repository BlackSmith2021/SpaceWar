import pygame

import random

from ships_and_bullet import WIN_HEIGHT, WIN_WIDTH, Ships, Bullet, Stars, BLACK

FPS = 60
WHITE = (255, 255, 255)
pygame.init()   # запуск игрового движка

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создание игрового окна

clock = pygame.time.Clock() # проверка заданой частоты
all_sprites = pygame.sprite.Group()  # создание группы для спрайтов

sh_l = Ships(WIN_WIDTH - 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\interprice.png', "sh_l", sc)  # обьект левого корабля
sh_r = Ships(0 + 30, WIN_HEIGHT//2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\titanik.png', "sh_r", sc)  # обьект правого корабля
all_sprites.add(sh_r, sh_l)  # добавление обьектов спрайтов в группу


arr = []  # массив для пуль левого корабля
arr_2 = []  # массив для пуль правого корабля
arr_stars = []

while True:  # запуск отрисовки
    for i in range(10):
        stars = Stars(random.randint(10, 1300), random.randint(10, 800), random.randint(1, 10), random.randint(5, 10), WHITE, sc)
    sc.fill(BLACK)  # отрисовка окна
    clock.tick(FPS)  # частота обновления кадро
    stars.draw()

    all_sprites.update()  # отрисовка группы спрайтов

    for i in pygame.event.get():  # запись действий за цикл
        if i.type == pygame.QUIT:  # если нажата кнопка выхода, выйти
            exit()
        if i.type == pygame.KEYUP:  # фиксация нажтия
            if i.key == pygame.K_q:  # создание обькта пули правого корабля и загрузка его в массив
                gun_1 = Bullet(sh_r.rect.x, sh_r.rect.y, "r", sc)
                all_sprites.add(gun_1)  # добавление в общую группу спрайтов для отрисовки
                arr_2.append(gun_1)

            if i.key == pygame.K_BACKSPACE:  # создание обькта пули левого корабля и загрузка его в массив
                gun_2 = Bullet(sh_l.rect.x, sh_l.rect.y, "l", sc)
                all_sprites.add(gun_2)
                arr.append(gun_2)

    for gun_1 in arr:  # проверка столкновеня корабля с пулей и удаление корабля
        if sh_r.rect.colliderect(gun_1.rect):
            sh_r.kill()
            arr.remove(gun_1)

    for gun_2 in arr_2:  # проверка столкновеня корабля с пулей и удаление корабля
        if sh_l.rect.colliderect(gun_2.rect):
            sh_l.kill()
            arr_2.remove(gun_2)

    pygame.display.update() # обновление экрана