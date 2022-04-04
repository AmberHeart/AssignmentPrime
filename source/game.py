import pygame
import sys
from start import Start
from supermarket import Supermarket
from start import Start

#pygame 初始化
pygame.init()

#设置主窗口

main_screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption("LOCK-DOWN IN USTC")
image_icon = pygame.image.load("../res/image/icon.png").convert()
pygame.display.set_icon(image_icon)

#开始界面
Start.Game0(main_screen)
result = Supermarket.Game1(main_screen)

#结束游戏
pygame.quit()
sys.exit()