import pygame
from my_errors import SpaceShipOutOffScreen

WIN_WIDTH = 1400
WIN_HEIGHT = 850
BLACK = (0, 0, 0)
LIME = (180, 255, 100)
ORANGE = (255, 100, 10)
RED = (255, 0, 0)

class Ships(pygame.sprite.Sprite):  # класс для космических кораблей
    def __init__(self, x, y, file_name, team, sc):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(file_name)
        self.team = team # атрибут определения кманды корабля
        self.sc = sc
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self): # общая функция отрисовки
        if self.team == "sh_l": # для левого корабля
            self.sc.blit(self.image, self.rect)
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.rect.x -= 10
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.rect.x += 10
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.rect.y -= 10
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.rect.y += 10
            if self.rect.x > WIN_WIDTH + self.image.get_width() or self.x < 0 - self.image.get_width():  # создание исключений
                raise SpaceShipOutOffScreen("корабль за пределами поля в горизонтальной плоскости")
            elif self.rect.y > WIN_HEIGHT + self.image.get_height() or self.rect.y < 0 - self.image.get_height():
                raise SpaceShipOutOffScreen("корабль за пределами поля в вертикальной плоскости")

        if self.team == "sh_r":   # для правого корабля
            self.sc.blit(self.image, self.rect)
            if pygame.key.get_pressed()[pygame.K_a]:
                self.rect.x -= 10
            if pygame.key.get_pressed()[pygame.K_d]:
                self.rect.x += 10
            if pygame.key.get_pressed()[pygame.K_w]:
                self.rect.y -= 10
            if pygame.key.get_pressed()[pygame.K_s]:
                self.rect.y += 10
            if self.rect.x > WIN_WIDTH + self.image.get_width() or self.rect.x < 0 - self.image.get_width():  # создание исключений
                raise SpaceShipOutOffScreen("корабль за пределами поля в горизонтальной плоскости")
            elif self.rect.y > WIN_HEIGHT + self.image.get_height() or self.rect.y < 0 - self.image.get_height():
                raise SpaceShipOutOffScreen("корабль за пределами поля в вертикальной плоскости")


class Bullet(pygame.sprite.Sprite):  # класс пуль
    def __init__(self, x, y, orient, sc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(LIME)
        self.x = x
        self.y = y
        self.orient = orient  # аргумент направления
        self.sc = sc
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.sc.blit(self.image, self.rect)
        if self.orient == "r":  # для координат правого корабля
            self.rect.x += 5
            if self.rect.left > WIN_WIDTH:
                self.kill()
        if self.orient == "l":   # для координат левого корабля
            self.rect.x -= 5
            if self.rect.right < 0:
                self.kill()