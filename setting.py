class Setting():
    """设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飛船的設置
        self.ship_speed_factor = 1.5

        #子弹设置

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_hetight = 15
        self.bullet_color = 60,60,60