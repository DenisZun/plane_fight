import pygame
from model_mixin import ModelMixin


# TODO 2.子弹类
class Bullet(ModelMixin):
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
