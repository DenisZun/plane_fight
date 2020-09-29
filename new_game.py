import random
import pygame
import sys
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768
enemy_lis = []


# TODO 6.模型基类
class Model(object):
    def __init__(self, x, y, window, image_path):
        self.position_x = x
        self.position_y = y
        self.window = window
        # 获取图片矩形
        self.image = pygame.image.load(image_path)
        self.img_rect = self.image.get_rect()

    def display(self):
        self.window.blit(self.image, (self.position_x, self.position_y))


# TODO 1.玩家飞机
class Plane(Model):
    def __init__(self, x, y, window, image_path):
        super(Plane, self).__init__(x, y, window, image_path)
        self.hero_bullet_image_path = "res/hero_bullet_7.png"
        self.bullet_list = []

    def fire(self):
        bullet_1 = Bullet(self.position_x + 5, self.position_y - 59, self.window, self.hero_bullet_image_path)
        bullet_2 = Bullet(self.position_x + 87, self.position_y - 59, self.window, self.hero_bullet_image_path)
        bullet_1.display()
        bullet_2.display()
        self.bullet_list.append([bullet_1, bullet_2])

    def show_bullet(self):
        delete_bullets = []
        for bullet_lis in self.bullet_list:
            for bullet in bullet_lis:
                if bullet.position_y > -59:
                    bullet.display()
                    bullet.move()
                else:
                    delete_bullets.append(bullet)

        for enemy in enemy_lis:
            for bullet_lis in self.bullet_list:
                for bullet in bullet_lis:
                    if bullet.is_hit_enemy(enemy):
                        enemy.is_hit = True
                        delete_bullets.append(bullet)

        for out_window_bullet in delete_bullets:
            for bullet_lis in self.bullet_list:
                if out_window_bullet in bullet_lis:
                    self.bullet_list.remove(bullet_lis)

    def move_left(self):
        if self.position_x > 0:
            self.position_x -= 5

    def move_right(self):
        if self.position_x <= WINDOW_WIDTH - self.img_rect[2]:
            self.position_x += 5

    def move_up(self):
        if self.position_y >= 0:
            self.position_y -= 5

    def move_down(self):
        if self.position_y <= WINDOW_HEIGHT - self.img_rect[3]:
            self.position_y += 5


# TODO 2.子弹类
class Bullet(Model):
    def move(self):
        self.position_y -= 5

    def enemy_move(self):
        self.position_y += 7

    def is_hit_enemy(self, enemy):
        """
        判断敌机中弹与否
        判断是否碰撞
        colliderect(
            pygame.Rect(self.x, self.y, 20, 31),
            pygame.Rect(enemy.x, enemy.y, 100, 68)
        )
        """
        if pygame.Rect.colliderect(
            pygame.Rect(self.position_x, self.position_y, 20, 73),
            pygame.Rect(enemy.position_x, enemy.position_y, 100, 68)
        ):
            return True  # TODO 敌机被击中
        else:
            return False  # TODO 敌机未击中


# TODO 3.敌机类
class Enemy(Model):
    def __init__(self, x, y, window, image_path):
        super(Enemy, self).__init__(x, y, window, image_path)
        self.enemy_bullet_image_path = "res/bullet_3.png"
        self.bullet_list = []
        self.is_hit = False

    def move(self):
        self.position_y += 5
        if self.position_y > WINDOW_HEIGHT:
            self.position_x = random.randint(0, random.randint(0, WINDOW_WIDTH - 100))
            self.position_y = 0

    def fire(self):
        # 敌机随机发射子弹
        random_num = random.randint(1, 50)
        if random_num == 20:
            bullet = Bullet(self.position_x + 40, self.position_y + 60, self.window, self.enemy_bullet_image_path)
            bullet.display()
            self.bullet_list.append(bullet)

    def show_bullet(self):
        delete_bullets = []
        for bullet in self.bullet_list:
            if bullet.position_y > WINDOW_HEIGHT:
                delete_bullets.append(bullet)
            else:
                bullet.display()
                bullet.enemy_move()

        for out_window_bullet in delete_bullets:
            self.bullet_list.remove(out_window_bullet)

    def display(self):
        if self.is_hit:
            self.position_x = random.randint(0, WINDOW_WIDTH - 100)
            self.position_y = 0
            self.is_hit = False

        self.window.blit(self.image, (self.position_x, self.position_y))


# TODO 4.背景类
class Background(Model):
    def move(self):
        # 实现背景的反复移动
        if self.position_y < WINDOW_HEIGHT:
            self.position_y += 1
        else:
            self.position_y = 0

    def display(self):
        self.window.blit(self.image, (self.position_x, self.position_y))
        self.window.blit(self.image, (self.position_x, self.position_y - self.img_rect[3]))


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
        self.bg_image_path = "res/img_bg_level_%d.jpg" % random.randint(1, 5)

        # 本地资源图英雄飞机图片路径
        self.hero_image_path = "res/hero2.png"
        self.hero_bullet_image_path = "res/bullet_10.png"
        # 敌机贴图
        self.enemy_image_path = "res/img-plane_%d.png" % random.randint(1, 7)
        # self.enemy_bullet_image_path = "res/bullet_3.png"
        # 加载背景音乐
        pygame.mixer.music.load("./res/bg2.ogg")
        # 加载音效
        self.boom_sound = pygame.mixer.Sound("./res/baozha.ogg")
        # 循环播放背景音乐
        pygame.mixer.music.play(-1)
        self.init_model()

    # TODO 5.6 模型初始实例化
    def init_model(self):
        # 创建实例对象
        # 玩家飞机实例
        self.player = Plane(196, 660, self.window, self.hero_image_path)
        # 地图背景实例
        self.background = Background(0, 0, self.window, self.bg_image_path)
        # 敌机对象实例
        self.enemy1 = Enemy(random.randint(120, WINDOW_WIDTH - 120), 0, self.window, "res/img-plane_%d.png" % random.randint(1, 7))
        self.enemy2 = Enemy(random.randint(120, WINDOW_WIDTH - 120), random.randint(0, WINDOW_HEIGHT - 68), self.window,
                            "res/img-plane_%d.png" % random.randint(1, 7))
        self.enemy3 = Enemy(random.randint(120, WINDOW_WIDTH - 120), random.randint(0, WINDOW_HEIGHT - 68), self.window,
                            "res/img-plane_%d.png" % random.randint(1, 7))
        self.enemy4 = Enemy(random.randint(120, WINDOW_WIDTH - 120), random.randint(0, WINDOW_HEIGHT - 68), self.window,
                            "res/img-plane_%d.png" % random.randint(1, 7))
        self.enemy5 = Enemy(random.randint(120, WINDOW_WIDTH - 120), random.randint(0, WINDOW_HEIGHT - 68), self.window,
                            "res/img-plane_%d.png" % random.randint(1, 7))
        self.enemy6 = Enemy(random.randint(120, WINDOW_WIDTH - 120), random.randint(0, WINDOW_HEIGHT - 68), self.window,
                            "res/img-plane_%d.png" % random.randint(1, 7))
        global enemy_lis
        enemy_lis = [self.enemy1, self.enemy2, self.enemy3, self.enemy4, self.enemy5, self.enemy6]
        self.enemy_lis = enemy_lis

    # TODO 5.2 描绘图形
    def draw(self):
        # 图片添加到窗口中
        # blit(添加到游戏窗口中图片对象, (0, 0)) (x, y) 坐标
        self.background.display()
        # 添加飞机
        self.player.display()
        for enemy in self.enemy_lis:
            enemy.display()
            enemy.show_bullet()
        # TODO bug记录
        self.player.show_bullet()

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
        mouse_state = pygame.mouse.get_pressed()
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
                    self.player.fire()
                    self.boom_sound.play()
                    print("发射子弹 biubiubiu")

            # 监听鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_state[0] == 1:
                    # 播放音效
                    self.player.fire()
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
            self.background.move()  # 调用背景移动操作，构造背景向下移动效果
            self.background.display()  # 刷新移动后的图片
            for enemy in self.enemy_lis:
                if not enemy.is_hit:
                    enemy.move()
                    enemy.fire()
            self.draw()
            self.event()
            self.update()
            time.sleep(0.01)


def main():
    # 主控制函数
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
