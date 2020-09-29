from model_mixin import ModelMixin

WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768


# TODO 4.背景类
class Background(ModelMixin):
    def move(self):
        # 实现背景的反复移动
        if self.position_y < WINDOW_HEIGHT:
            self.position_y += 1
        else:
            self.position_y = 0

    def display(self):
        self.window.blit(self.image, (self.position_x, self.position_y))
        self.window.blit(self.image, (self.position_x, self.position_y - self.img_rect[3]))