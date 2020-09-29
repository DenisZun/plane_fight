import random
import pygame
from model_mixin import ModelMixin
from bullet import Bullet

WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768


# TODO 3.敌机类
class Enemy(ModelMixin):
    def __init__(self, x, y, window, image_path):
        super(Enemy, self).__init__(x, y, window, image_path)
        self.enemy_bullet_image_path = "res/bullet_3.png"
        self.bullet_list = []
        self.is_hit = False  # 判断是否中弹
        self.animax = 0  # 爆炸动画索引
        self.boom_sound = pygame.mixer.Sound("./res/bomb.wav")  # 中弹后爆炸音效

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
        # 飞机爆炸效果在中弹后才调用
        if self.is_hit:
            # 敌机中弹后先播放爆炸动画
            self.explosion()
            # 添加爆炸音效
            self.boom_sound.play()
        # 在爆炸动画结束后应重新贴敌机图
        self.window.blit(self.image, (self.position_x, self.position_y))

    def explosion(self):
        # 敌机在中弹后的爆炸效果
        if self.animax >= 21:
            self.position_x = random.randint(0, WINDOW_WIDTH - 100)
            self.position_y = 0
            self.is_hit = False
            self.animax = 0
            self.image = pygame.image.load("res/img-plane_%d.png" % (random.randint(1, 7)))
            return
        self.image = pygame.image.load("res/bomb-%d.png" % (self.animax//3 + 1))
        self.animax += 1
