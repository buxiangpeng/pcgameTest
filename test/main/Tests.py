import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 1000, 900
screen = pygame.display.set_mode(size)
color = 255,0,0
width = 2
screen.fill((0,255,255))

oldXY = (0,0)
newXY = (0,0)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
    #初始化
    pygame.draw.line(screen, color, oldXY, newXY, width)
    pygame.display.update()

    #获取鼠标点击状态
    status = pygame.mouse.get_pressed()
    if status[0] == 1:
        newXY = pygame.mouse.get_pos()
        pygame.draw.line(screen, color, oldXY, newXY, width)
        pygame.display.update()
        oldXY = newXY