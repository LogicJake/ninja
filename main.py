import random
import pygame
import time
from pygame.locals import *
from sys import exit

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

stime = 0
flag = False
sindex = []

def check(screen,index,x,y):        #检查是否接近圆点
    global flag,sindex
    x += mouse_cursor.get_width() / 2
    y += mouse_cursor.get_height() / 2
    i = 0
    for d in index:
        if pow(x-d['x'], 2)+pow(y-d['y'],2) <= pow(zhijing/2,2):
            if flag and i == 0:
                eindex = pygame.mouse.get_pos()
                print("移动距离为："+str(pow(sindex[0] - eindex[0], 2) + pow(sindex[1] - eindex[1], 2)))
                sindex = []
                print("时间为："+str(time.time()-stime))
                flag = False
            pygame.draw.circle(screen, green, [d['x'], d['y']], zhijing)
        i += 1
if __name__ == '__main__':
    zhijing_index = random.randrange(3)
    num_index = random.randrange(3)
    zhijing = zhijings[zhijing_index]
    num = nums[num_index]

    print("直径为："+str(zhijing))
    print("数量为："+str(num))

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
    index = []
    for i in range(num):
        tmp = {}
        tmp['x'] = random.randrange(width)
        tmp['y'] = random.randrange(height)
        index.append(tmp)

    x_temp = 0
    y_temp = 0
    while True:
        # 游戏主循环
        for event in pygame.event.get():
            screen.blit(mouse_cursor, (x_temp, y_temp))
            screen.blit(mouse_cursor2, (x_temp - offsetx, y_temp - offsety))
            screen.blit(mouse_cursor3, (x_temp, y_temp - offsety))
            screen.blit(mouse_cursor4, (x_temp - offsetx, y_temp))
            if event.type == KEYDOWN:
                if event.key == K_1:  # 获取键盘字母a
                    choice = 1
                elif event.key == K_2:  # 获取键盘空格键
                    choice = 2
                elif event.key == K_3:  # 获取键盘左键
                    choice = 3
                elif event.key == K_4:
                    choice = 4
                elif event.key == K_5:
                    choice = 5
                elif event.type == K_ESCAPE:
                    # 接收到退出事件后退出程序
                    exit()
                elif event.key == K_8:
                    stime = time.time()
                    sindex = pygame.mouse.get_pos()
                    flag = True

        screen.fill([255, 255, 255])  # 用白色填充窗口

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
            screen.blit(mouse_cursor2, (x-offsetx, y-offsety))
            screen.blit(mouse_cursor3, (x, y-offsety))
            screen.blit(mouse_cursor4, (x-offsetx, y))
            check(screen, index, x - offsetx, y - offsety)
            check(screen, index, x, y - offsety)
            check(screen, index, x - offsetx, y)
            check(screen, index, x, y)
        elif choice == 1:
            screen.blit(mouse_cursor, (x_temp, y_temp))
            screen.blit(mouse_cursor2, (x - offsetx, y - offsety))
            screen.blit(mouse_cursor3, (x_temp, y_temp - offsety))
            screen.blit(mouse_cursor4, (x_temp - offsetx, y_temp))
            check(screen,index,x-offsetx,y-offsety)
        elif choice == 2:
            screen.blit(mouse_cursor, (x_temp, y_temp))
            screen.blit(mouse_cursor2, (x_temp-offsetx, y_temp-offsety))
            screen.blit(mouse_cursor3, (x, y-offsety))
            screen.blit(mouse_cursor4, (x_temp-offsetx, y_temp))
            check(screen, index,x, y-offsety)
        elif choice == 3:
            screen.blit(mouse_cursor, (x_temp, y_temp))
            screen.blit(mouse_cursor2, (x_temp-offsetx, y_temp-offsety))
            screen.blit(mouse_cursor3, (x_temp, y_temp-offsety))
            screen.blit(mouse_cursor4, (x-offsetx, y))
            check(screen, index,x-offsetx, y)
        elif choice == 4:
            screen.blit(mouse_cursor, (x, y))
            screen.blit(mouse_cursor2, (x_temp-offsetx, y_temp-offsety))
            screen.blit(mouse_cursor3, (x_temp, y_temp-offsety))
            screen.blit(mouse_cursor4, (x_temp-offsetx, y_temp))
            check(screen, index,x,y)
        elif choice == 5:
            screen.blit(mouse_cursor, (x, y))
            screen.blit(mouse_cursor2, (x - offsetx, y - offsety))
            screen.blit(mouse_cursor3, (x, y - offsety))
            screen.blit(mouse_cursor4, (x - offsetx, y))
            check(screen, index, x - offsetx, y - offsety)
            check(screen, index, x, y - offsety)
            check(screen, index, x - offsetx, y)
            check(screen, index, x, y)

        pygame.display.update()
        # 刷新一下画面