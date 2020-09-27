# 导入模块
# import pygame
# import sys

import pygame
import sys

# pygame进行实例化
pygame.init()

# 创建游戏窗口-> 返回一个游戏窗口对象
# set_mode([400, 400]) -> (列表)[游戏窗口的宽度, 游戏窗口的高度]
# 单位是像素
window = pygame.display.set_mode([512, 768])

# 设置游戏窗口的标题
pygame.display.set_caption("飞机大战")

# 加载本地资源图片 返回一个图片对象
logo_image = pygame.image.load("res/app.ico")
# 设置游戏窗口的logo
pygame.display.set_icon(logo_image)

# 游戏背景图片对象添加到游戏窗口中
# 加载本地资源图片 返回一个游戏背景图片对象
bg_image = pygame.image.load("res/img_bg_level_1.jpg")


# 加载本地资源图片 返回一个英雄飞机图片对象
hero_image = pygame.image.load("res/hero2.png")
# 加载背景音乐
pygame.mixer.music.load("./res/bg2.ogg")
# 加载音效
boom_sound = pygame.mixer.Sound("./res/baozha.ogg")
# 循环播放背景音乐
pygame.mixer.music.play(-1)

# 我方初始位置 记录x轴, y轴
x, y = 196, 660

# 死循环 在死循环中监听无论鼠标点击事件 或者键盘按键的事件
while True:
    # 图片添加到窗口中
    # blit(添加到游戏窗口中图片对象, (0, 0)) (x, y) 坐标
    window.blit(bg_image, (0, 0))
    # 添加飞机
    window.blit(hero_image, (x, y))
    # 记得刷新游戏窗口
    pygame.display.update()
    # my_x += 3
    # 获取所有游戏窗口的中的事件监听-> 列表
    event_list = pygame.event.get()
    # 遍历所有的事件
    for event in event_list:
        # 判断如果是鼠标点击了
        if event.type == pygame.QUIT:
            # 退出游戏
            # 停止pygame 游戏引擎
            pygame.quit()
            # 退出程序
            sys.exit()

        # 监听esc键按下
        if event.type == pygame.KEYDOWN:
            # 判断是否按得是esc
            if event.key == pygame.K_ESCAPE:
                # 退出游戏
                # 停止pygame 游戏引擎
                pygame.quit()
                # 退出程序
                sys.exit()
            # 开火方法
            if event.key == pygame.K_SPACE:
                # 播放音效
                boom_sound.play()
                print("发射子弹 biubiubiu")

    # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
    pressed_keys = pygame.key.get_pressed()
    # 判断向上的按键是否在长按(1)
    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        y -= 5
        print("向上")

    # 判断向下的按键是否在长按(1)
    if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        y += 5
        print("向下")

    # 判断向左的按键是否在长按(1)
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        x -= 5
        print("向左")

    # 判断向右的按键是否在长按(1)
    if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        x += 5
        print("向右")



