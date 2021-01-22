

import sys
import pygame
from setting import Setting
from ship import Ship

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 从setting类中实例化配置
    ai_settings = Setting()
    # 创建游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # 游戏窗口标题
    pygame.display.set_caption("Alien Invasion")

    #创建一个飞船
    ship = Ship(screen)
    # 设置背景颜色
    bg_color=(230,230,230)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        
        # 每次循环时都会重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()
