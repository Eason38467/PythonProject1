

import sys
import pygame
from setting import Setting
from game_stats import GameStats
from ship import Ship
#from alien import Alien  不需要在这里创建外星人， 与子弹创建类似
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
    #创建一个存储游戏统计的实例
    stats = GameStats(ai_settings)
    #创建一个飞船
    ship = Ship(ai_settings,screen)
    #创建一个子弹的组
    bullets=Group()
    # 设置背景颜色
    bg_color=(230,230,230)
    #创建一个外星人
    #alien = Alien(ai_settings,screen)
    #创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen ,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        #下面的这个print用来在终端接口看子弹数量，可以删除
        print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
