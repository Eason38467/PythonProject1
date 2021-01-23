

import sys
import pygame
from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group

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
    ship = Ship(ai_settings,screen)
    #创建一个子弹的组
    bullets=Group()
    # 设置背景颜色
    bg_color=(230,230,230)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen ,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        #下面的这个print用来在终端接口看子弹数量，可以删除
        print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
