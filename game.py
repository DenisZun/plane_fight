import pygame


pygame.init()
# 创建窗口
window = pygame.display.set_mode([400, 400])

# 设置窗口标题
pygame.display.set_caption("窗口标题")

# 加载资源图片，返回图片对象
logo_image = pygame.image.load("res/game.ico")

# 设置窗口图标
pygame.display.set_icon(logo_image)

# 加载资源图片，返回图片对象
bg_image = pygame.image.load("res/img_bg_level_2.jpg")

# 指定坐标，将图片绘制到窗口
window.blit(bg_image, (0, 0))

# 不管做了什么操作，最后刷新一下画面，重新加载。
pygame.display.update()