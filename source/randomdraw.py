import sys
import pygame
import random

class Randdraw:
    
    def spawn_item():
        judge_num = random.randint(0,99)
        if 95 <= judge_num:
            #legendary
            return 0
        elif 80 <= judge_num:
            #epic
            return 1
        elif 50 <= judge_num:
            #rare
            return 2
        else:
            #common
            return 3
        
    def getdraw(start_item):

        draw_result = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0,0]

        for i in range(0,4):
            for j in range(0,start_item[i]):
                draw_result[i][Randdraw.spawn_item()] += 1

        draw_result[4] = start_item[4]
        draw_result[5] = start_item[5]
        return draw_result
