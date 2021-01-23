import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示一个外星人单位'''
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人的图像，并设置其rect属性

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人初始化在屏幕左上角

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人位置

        self.x = float(self.rect.x)

    def check_edges(self):
        """如果有外星人位于屏幕边缘，就返回True"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)