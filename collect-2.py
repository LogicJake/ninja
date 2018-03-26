#coding=utf-8
import random
import pygame
import time

from math import *
from pygame.locals import *
from sys import exit
import csv
mouse_image_filename = 'cursor.png'

white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,0,0)
blue = (0,0,255)
#屏幕大小
width = 1080
height = 600
#鼠标偏移
offsetx = 500
offsety = 400
#随机变量
zhijings = [20,30,50]
nums = [1,10,20]

my_dict = {
    0:"00",
    1:"01",
    2:"02",
    3:"10",
    4:"11",
    5:"12",
    6:"20",
    7:"21",
    8:"22"
}

stime = 0
flag = False
sindex = []

start_x = width-100
start_y = height-50

zhijing = 0
num = 0

index = []
res = []

x_temp = 0
y_temp = 0

def min_distance(index):
    global res
    pos = []
    pos.append(width-100)
    pos.append(height-50)
    x = index['x']
    y = index['y']
    distance1 = round(pow(sqrt(pow(pos[0]-x,2)+pow(pos[1]-y,2))-10-zhijing/2,2),1)
    distance2 = round(pow(sqrt(pow(pos[0]-offsetx-x,2)+pow(pos[1]-y,2))-10-zhijing/2,2),1)
    distance3 = round(pow(sqrt(pow(pos[0]-offsetx-x,2)+pow(pos[1]-offsety-y,2))-10-zhijing/2,2),1)
    distance4 = round(pow(sqrt(pow(pos[0]-x,2)+pow(pos[1]-offsety-y,2))-10-zhijing/2,2),1)
    res.append(str(min(distance1,distance2,distance3,distance4)))

def checkstart():
    global flag,stime,sindex
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    if pow(x - start_x, 2) + pow(y - start_y, 2) <= pow(20 / 2, 2) and not flag:
        pygame.draw.circle(screen, green, [start_x, start_y], 20)
        res.append(str(zhijing))
        res.append(str(num))
        min_distance(index[0])
        stime = time.time()
        sindex = pygame.mouse.get_pos()
        flag = True
    elif pow(x - start_x, 2) + pow(y - start_y, 2) <= pow(20 / 2, 2) and flag:
        pygame.draw.circle(screen, green, [start_x, start_y], 20)

def check(screen,index,x,y):        #检查是否接近圆点
    global flag,sindex,res
    x += mouse_cursor.get_width() / 2
    y += mouse_cursor.get_height() / 2
    i = 0
    num = 0
    for d in index:
        if pow(x-d['x'], 2)+pow(y-d['y'],2) <= pow(zhijing/2,2):
            num += 1
            if flag and i == 0:
                eindex = pygame.mouse.get_pos()
                res.append(str(pow(sindex[0] - eindex[0], 2) + pow(sindex[1] - eindex[1], 2)))
                sindex = []
                res.append(str(time.time()-stime))
                flag = False
                res.append(str(num))
                print(res)
                csv_file = open('data.csv', 'a+',newline="")
                myWriter = csv.writer(csv_file)
                myWriter.writerow(res)
                csv_file.close()
                res = []
            pygame.draw.circle(screen, green, [d['x'], d['y']], zhijing)
        i += 1

def init(cishu):
    global zhijing,num,x_temp,y_temp,index
    index = []
    zhijing_index = int(my_dict[cishu][0])
    num_index = int(my_dict[cishu][1])
    zhijing = zhijings[zhijing_index]
    num = nums[num_index]
    for i in range(num):
        tmp = {}
        tmp['x'] = random.randrange(width)
        tmp['y'] = random.randrange(height)
        index.append(tmp)

    x_temp = 0
    y_temp = 0

if __name__ == '__main__':
    cishu = 0
    init(cishu)
    pygame.init()
    # 初始化pygame,为使用硬件做准备
    screen = pygame.display.set_mode((width, height), 0, 32)
    # 创建了一个窗口
    pygame.display.set_caption("ninja")
    # 设置窗口标题
    mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
    mouse_cursor2 = pygame.image.load(mouse_image_filename).convert_alpha()
    mouse_cursor3 = pygame.image.load(mouse_image_filename).convert_alpha()
    mouse_cursor4 = pygame.image.load(mouse_image_filename).convert_alpha()
    # 加载并转换图像
    choice = 0

    pygame.mouse.set_pos(width - 200, height - 100)  # 固定光标位置

    while True:
        # 游戏主循环
        for event in pygame.event.get():
            screen.blit(mouse_cursor, (x_temp, y_temp))
            # screen.blit(mouse_cursor2, (x_temp - offsetx, y_temp - offsety))
            # screen.blit(mouse_cursor3, (x_temp, y_temp - offsety))
            screen.blit(mouse_cursor4, (x_temp - offsetx, y_temp))
            if event.type == KEYDOWN:
                if event.key == K_1:
                    choice = 1
                elif event.key == K_2:
                    choice = 2
                elif event.key == K_3:
                    choice = 3
                elif event.key == K_4:
                    choice = 4
                elif event.key == K_5:
                    choice = 5
                elif event.type == QUIT:
                    # 接收到退出事件后退出程序
                    exit()
                elif event.key == K_9:
                    choice = 0
                    pygame.draw.circle(screen, gray, [start_x, start_y], zhijing)
                    cishu += 1
                    if cishu > 8:       #退出实验
                        break
                    init(cishu)
                    pygame.mouse.set_pos(width - 200, height - 100)  # 固定光标位置


        screen.fill([255, 255, 255])  # 用白色填充窗口

        pygame.draw.circle(screen, gray, [start_x, start_y], 20)
        checkstart()

        i = 0
        for d in index:
            if i == 0:
                pygame.draw.circle(screen, black, [d['x'], d['y']], zhijing)
            else:
                pygame.draw.circle(screen, red, [d['x'], d['y']],zhijing)
            i += 1

        pygame.mouse.set_visible(False)


        x, y = pygame.mouse.get_pos()
        # 获得鼠标位置
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        # 计算光标的左上角位置
        if choice == 0:
            x_temp = x
            y_temp = y
            screen.blit(mouse_cursor, (x, y))
            # screen.blit(mouse_cursor2, (x-offsetx, y-offsety))
            # screen.blit(mouse_cursor3, (x, y-offsety))
            screen.blit(mouse_cursor4, (x-offsetx, y))
            # check(screen, index, x - offsetx, y - offsety)
            # check(screen, index, x, y - offsety)
            check(screen, index, x - offsetx, y)
            check(screen, index, x, y)
        # elif choice == 1:
        #     screen.blit(mouse_cursor, (x_temp, y_temp))
        #     screen.blit(mouse_cursor2, (x - offsetx, y - offsety))
        #     screen.blit(mouse_cursor3, (x_temp, y_temp - offsety))
        #     screen.blit(mouse_cursor4, (x_temp - offsetx, y_temp))
        #     check(screen,index,x-offsetx,y-offsety)
        # elif choice == 2:
        #     screen.blit(mouse_cursor, (x_temp, y_temp))
        #     screen.blit(mouse_cursor2, (x_temp-offsetx, y_temp-offsety))
        #     screen.blit(mouse_cursor3, (x, y-offsety))
        #     screen.blit(mouse_cursor4, (x_temp-offsetx, y_temp))
        #     check(screen, index,x, y-offsety)
        elif choice == 3:
            screen.blit(mouse_cursor, (x_temp, y_temp))
            # screen.blit(mouse_cursor2, (x_temp-offsetx, y_temp-offsety))
            # screen.blit(mouse_cursor3, (x_temp, y_temp-offsety))
            screen.blit(mouse_cursor4, (x-offsetx, y))
            check(screen, index,x-offsetx, y)
        elif choice == 4:
            screen.blit(mouse_cursor, (x, y))
            # screen.blit(mouse_cursor2, (x_temp-offsetx, y_temp-offsety))
            # screen.blit(mouse_cursor3, (x_temp, y_temp-offsety))
            screen.blit(mouse_cursor4, (x_temp-offsetx, y_temp))
            check(screen, index,x,y)
        elif choice == 5:
            screen.blit(mouse_cursor, (x, y))
            # screen.blit(mouse_cursor2, (x - offsetx, y - offsety))
            # screen.blit(mouse_cursor3, (x, y - offsety))
            screen.blit(mouse_cursor4, (x - offsetx, y))
            # check(screen, index, x - offsetx, y - offsety)
            # check(screen, index, x, y - offsety)
            check(screen, index, x - offsetx, y)
            check(screen, index, x, y)

        pygame.display.update()
        # 刷新一下画面
