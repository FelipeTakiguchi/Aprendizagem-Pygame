import pygame
from sys import exit
import numpy as np

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Drag")
clock = pygame.time.Clock()

player_sprite = "torre.png"
grass_sprite = "grama.png"

class Tower:
    def __init__(self, sprite):
        self.surf = pygame.image.load(sprite).convert_alpha()
        self.rect = self.surf.get_rect(center=(400, 400))
        self.isDragging = False
        self.isDragabble = True

    def draw(self):
        screen.blit(self.surf, self.rect)

class Grass:
    def __init__(self, sprite, x, y):
        self.surf = pygame.image.load(sprite).convert_alpha()
        self.rect = self.surf.get_rect(center=(x, y))
        self.isDragging = False

    def draw(self):
        screen.blit(self.surf, self.rect)

class Background:
    def __init__(self, color):
        self.surf = pygame.Surface((800, 800))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=(400, 400))

    def get_rect(self):
        return self.rect

    def draw(self):
        screen.blit(self.surf, self.rect)

t = Tower(player_sprite)

grass = [[Grass, Grass, Grass, Grass, Grass],
         [Grass, Grass, Grass, Grass, Grass],
         [Grass, Grass, Grass, Grass, Grass],
         [Grass, Grass, Grass, Grass, Grass],
         [Grass, Grass, Grass, Grass, Grass],
         [Grass, Grass, Grass, Grass, Grass]]

for i in range(5):
    for l in range(5):
        grass[l][i] = Grass(grass_sprite, 75 + ((l) * 150), 75 + ((i) * 150))

bg = Background('black')
pygame.mouse.set_visible(False)  # hide the cursor+

cursor = pygame.image.load('mouse_cursor.png').convert_alpha()
cursor_rect = cursor.get_rect(center=pygame.mouse.get_pos())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                t.isDragabble = True
                t.rect.center = (400, 400)


        if t.isDragabble:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if t.rect.collidepoint(pygame.mouse.get_pos()):
                    t.isDragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                if t.isDragging:
                    if t.rect.collidepoint(pygame.mouse.get_pos()):
                        t.isDragging = False
                    for i in range(5):
                        for l in range(5):
                            if grass[l][i].rect.collidepoint(t.rect.center):
                                t.rect.center = grass[l][i].rect.center
                                t.isDragabble = False

    if t.isDragging:
        t.rect.center = pygame.mouse.get_pos()

    bg.draw()

    for i in range(5):
        for l in range(5):
            grass[l][i].draw()

    t.draw()
    screen.blit(cursor, (pygame.mouse.get_pos()))

    pygame.display.update()
    clock.tick(60)
