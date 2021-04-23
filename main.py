import pygame

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

x = WIN_WIDTH // 2  # скрываем за левой границей
y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали
w = 30
h = 70
naprav = 1

van = Van(sc, 700, 700, 25, 50)

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

    pygame.draw.rect(sc, BLACK, (x - h // 2, y - w // 2, h, w))
    pygame.draw.rect(sc, BLACK, (x - w // 2, y - h // 2, w, h))

    if h >= 100 or h <= 1:  # если переменная(длинна для одного, высота для другог) выходит за устанновленные рамки
        naprav *= -1  # ее значение умножается на -1 и принимает отрицательное значение в случае если она больше условия
        h += 8 * naprav  # положительное в случае если меньше
    else:
        h += 5 * naprav

    for gun_1 in arr:  # проверка столкновеня корабля с пулей и удаление корабля
        if sh_r.rect.colliderect(gun_1.rect):
            sh_r.kill()
            arr.remove(gun_1)

    for gun_2 in arr_2:  # проверка столкновеня корабля с пулей и удаление корабля
        if sh_l.rect.colliderect(gun_2.rect):
            sh_l.kill()
            arr_2.remove(gun_2)

    pygame.display.update()  # обновление экрана
