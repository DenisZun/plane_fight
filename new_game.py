import pygame
import sys

WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768


# TODO 1.玩家飞机
class Plane(object):
    def __init__(self, x, y, window, image_path):
        self.position_x = x
        self.position_y = y
        self.window = window
        self.image = pygame.image.load(image_path)

    def fire(self):
        pass

    def display(self):
        self.window.blit(self.image, (self.position_x, self.position_y))

    def move_left(self):
        self.position_x -= 5

    def move_right(self):
        self.position_x += 5

    def move_up(self):
        self.position_y -= 5

    def move_down(self):
        self.position_y += 5


# TODO 2.子弹类
class Bullet(object):
    pass


# TODO 3.敌机类
class Enemy(object):
    pass


# TODO 4.背景类
class Background(object):
    pass


# TODO 5.游戏类
class Game(object):
    def __init__(self):
        # TODO 5.1 游戏基本配置信息（公共变量或只执行一遍的）
        # pygame进行实例化
        pygame.init()

        # 创建游戏窗口-> 返回一个游戏窗口对象
        # set_mode([400, 400]) -> (列表)[游戏窗口的宽度, 游戏窗口的高度]
        # 单位是像素
        self.window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

        # 设置游戏窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载本地资源图片 返回一个图片对象
        self.logo_image = pygame.image.load("res/app.ico")
        # 设置游戏窗口的logo
        pygame.display.set_icon(self.logo_image)

        # 游戏背景图片对象添加到游戏窗口中
        # 加载本地资源图片 返回一个游戏背景图片对象
        self.bg_image = pygame.image.load("res/img_bg_level_1.jpg")

        # 本地资源图英雄飞机图片路径
        self.hero_image_path = "res/hero2.png"
        # 加载背景音乐
        pygame.mixer.music.load("./res/bg2.ogg")
        # 加载音效
        self.boom_sound = pygame.mixer.Sound("./res/baozha.ogg")
        # 循环播放背景音乐
        pygame.mixer.music.play(-1)

        # 创建实例对象
        self.player = Plane(196, 660, self.window, self.hero_image_path)

    # TODO 5.2 描绘图形
    def draw(self):
        # 图片添加到窗口中
        # blit(添加到游戏窗口中图片对象, (0, 0)) (x, y) 坐标
        self.window.blit(self.bg_image, (0, 0))
        # 添加飞机
        self.player.display()

    # TODO 5.3 退出游戏
    def quit(self):
        # 退出游戏
        # 停止pygame 游戏引擎
        pygame.quit()
        # 退出程序
        sys.exit()

    # TODO 5.4 监听事件
    def event(self):
        # 获取所有游戏窗口的中的事件监听-> 列表
        event_list = pygame.event.get()
        # 遍历所有的事件
        for event in event_list:
            # 判断如果是鼠标点击了
            if event.type == pygame.QUIT:
                self.quit()

            # 监听esc键按下
            if event.type == pygame.KEYDOWN:
                # 判断是否按得是esc
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                # 开火方法
                if event.key == pygame.K_SPACE:
                    # 播放音效
                    self.boom_sound.play()
                    print("发射子弹 biubiubiu")

        # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
        pressed_keys = pygame.key.get_pressed()
        # 判断向上的按键是否在长按(1)
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.player.move_up()

        # 判断向下的按键是否在长按(1)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.player.move_down()

        # 判断向左的按键是否在长按(1)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.player.move_left()

        # 判断向右的按键是否在长按(1)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.player.move_right()

    # TODO 5.5 刷新窗口
    def update(self):
        # 记得刷新游戏窗口
        pygame.display.update()

    # TODO 5.0 启动游戏
    def run(self):
        # 死循环 在死循环中监听无论鼠标点击事件 或者键盘按键的事件
        while True:
            self.draw()
            self.event()
            self.update()


def main():
    # 主控制函数
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
