import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像,rect 是矩阵的缩写， 获取其外接矩阵
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飛船的属性center中存储最小数值
        self.center = float(self.rect.centerx)

        #飞船移动标识
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据飞船的移动标致调整飞船位置"""
        #if self.moving_right:
        #    self.center += self.ai_settings.ship_speed_factor
        #if self.moving_left:
         #   self.center -= self.ai_settings.ship_speed_factor
        
        #更新飞船的 center值而不是rect

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center 更新rect 对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)