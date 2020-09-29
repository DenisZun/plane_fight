import pygame


# TODO 6.模型基类
class ModelMixin(object):
    def __init__(self, x, y, window, image_path):
        self.position_x = x
        self.position_y = y
        self.window = window
        # 获取图片矩形
        self.image = pygame.image.load(image_path)
        self.img_rect = self.image.get_rect()

    def display(self):
        self.window.blit(self.image, (self.position_x, self.position_y))