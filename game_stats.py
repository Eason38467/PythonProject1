class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        #self.game_active = True
        self.reset_stats()
        #让游戏一开始处于非活动的状态
        self.game_active = False


    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
