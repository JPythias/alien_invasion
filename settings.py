# JawnPythias
# date:23/02/2024
class Settings:
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.5
        self.bullet_speed = 0.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 0.8
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1
        self.ship_limit = 3