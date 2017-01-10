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
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    i = 0
    while i < 5:
        StarList.append(Star.star(Random.getRandomCoordinat(WIN_WIDTH, WIN_HEIGHT)))
        i = i+1

    CenterOfMass = Star.star([0,0])
    while 1:  # Основной цикл программы
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == pygame.QUIT:
                sys.exit()
        i = 0

        screen.blit(bg, (0, 0))
        i = 0
        CenterOfMass.setPosition(Physics.getCenterOfMassPosition(StarList))
        CenterOfMass.setMass(Physics.getAllMass(StarList))
        while i < len(StarList):
            StarList[i].CalculateAcceleration(CenterOfMass)
            StarList[i].CalculatePosition()
            pygame.draw.circle(screen, white, StarList[i].getPosition(), 10)
            i = i +1
          # Каждую итерацию необходимо всё перерисовывать
        pygame.draw.circle(screen, yellow, CenterOfMass.getPosition(), 10)
        pygame.display.update()
        pygame.time.delay(150)# обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()




