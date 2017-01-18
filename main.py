#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
import Star
import Random
import sys
import array
import Physics
WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = ( WIN_WIDTH , WIN_HEIGHT )
BACKGROUND_COLOR = "#000000"
white = [255, 255, 255]
yellow = [255, 255, 0]
StarList = list()


def main():

    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Gravity Points")  # Пишем в шапку

    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    border = [WIN_WIDTH, WIN_HEIGHT]
    center = [WIN_WIDTH/2,WIN_HEIGHT/2]
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    i = 0

    StarList.append(Star.star(center))
    StarList[0].setVelosity([0,0])
    StarList[0].setMass(10000)

    StarList.append(Star.star([WIN_WIDTH/2 + 150,WIN_HEIGHT/2]))
    StarList[1].setVelosity([0,-3])
    StarList[1].setMass(10)


    StarList.append(Star.star([WIN_WIDTH/2 + 300,WIN_HEIGHT/2 + 40]))
    StarList[2].setVelosity([0,-1])
    StarList[2].setMass(1)

    counter = 0
    while 1:  # Основной цикл программы
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    StarList.append(Star.star(event.pos))
        i = 0

        screen.blit(bg, (0, 0))
        i = 0


        while i < len( StarList ):
            StarList[0].setPosition(center)
            StarList[i].CalculateVelosity(StarList , i)
            StarList[i].CalculatePosition(border)
            pygame.draw.circle(screen, white, StarList[i].getPosition(), 3)
            i = i + 1
          # Каждую итерацию необходимо всё перерисовывать
        pygame.display.update()
        pygame.time.delay(1)# обновление и вывод всех изменений на экран



if __name__ == "__main__":
    main()




