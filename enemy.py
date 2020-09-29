import random
from model_mixin import ModelMixin
from bullet import Bullet

WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768


# TODO 3.敌机类
class Enemy(ModelMixin):
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
