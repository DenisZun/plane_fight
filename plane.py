from model_mixin import ModelMixin
from bullet import Bullet
# from game import enemy_lis

WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768


# TODO 1.玩家飞机
class Plane(ModelMixin):
    def __init__(self, x, y, window, image_path, enemy_lis):
        super(Plane, self).__init__(x, y, window, image_path)
        self.hero_bullet_image_path = "res/hero_bullet_7.png"
        self.bullet_list = []
        self.enemy_lis = enemy_lis

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

        for enemy in self.enemy_lis:
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
