import pygame
import random

from ships_and_bullet import WIN_HEIGHT, WIN_WIDTH, Ships, Bullet, BLACK, Van

FPS = 60

pygame.init()  # запуск игрового движка

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создание игрового окна
background = pygame.image.load('C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\room.png')
background_rect = background.get_rect()

clock = pygame.time.Clock()  # проверка заданой частоты
all_sprites = pygame.sprite.Group()  # создание группы для спрайтов

sh_l = Ships(WIN_WIDTH - 30, WIN_HEIGHT // 2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\interprice.png', "sh_l",
             sc)  # обьект левого корабля
sh_r = Ships(0 + 30, WIN_HEIGHT // 2, 'C:\\Users\\kulpa\\Documents\\Pyton\\SpaceWar\\titanik.png', "sh_r",
             sc)  # обьект правого корабля
all_sprites.add(sh_r, sh_l)  # добавление обьектов спрайтов в группу

arr_van = []
arr = []  # массив для пуль левого корабля
arr_2 = []  # массив для пуль правого корабля

while True:  # запуск отрисовки
    sc.fill(BLACK)  # отрисовка окна
    sc.blit(background, background_rect)  # отрисовка фона
    all_sprites.draw(sc)
    clock.tick(FPS)  # частота обновления кадро

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

    for i in range(3):  # создается три обьекта класса Van с рандомным местоположением и добавляются в массив
        van = Van(sc, random.randint(1, 1600), random.randint(1, 1600), 5, 5)
        arr_van.append(van)

    for i in arr_van:  # отрисовка массива обьькта из массива и удаление элемента по индексу 0
        i.update()
        if len(arr_van) > 200:
            arr_van.pop(0)

    for gun_1 in arr:  # проверка столкновеня корабля с пулей и удаление корабля
        if sh_r.rect.colliderect(gun_1.rect):
            sh_r.kill()
            arr.remove(gun_1)

    for gun_2 in arr_2:  # проверка столкновеня корабля с пулей и удаление корабля
        if sh_l.rect.colliderect(gun_2.rect):
            sh_l.kill()
            arr_2.remove(gun_2)

    pygame.display.update()  # обновление экрана
