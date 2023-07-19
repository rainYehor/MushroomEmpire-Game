import pygame
import models
from settings import *


class Button(models.Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def check_click(self,mouse_pos):
        if self.rect.x < mouse_pos[0] < self.rect.x + self.rect.width:
            if self.rect.y < mouse_pos[1] < self.rect.y + self.rect.height:
                return True 
                
                
          
                
menu_button_start = Button(x = 490, y = 150, width = 300, height = 120, img_path = 'images/menu_button/play_button.png')
menu_button_settings = Button(x = 440, y = 300, width = 400, height = 120, img_path = 'images/menu_button/settings_button.png')
menu_button_exit = Button(x = 490, y = 450, width = 300, height = 120, img_path = 'images/menu_button/exit_button.png')
button_back = Button(x = 0, y = 720-150, width = 200, height = 100, img_path = 'images/menu_button/back_button.png')
settings_button_music = Button(x = 565, y = 350, width = 150, height = 100, img_path = 'images/menu_button/music_on.png')
#settings_button_sounds = Button(x = 565, y = 200, width = 150, height = 100, img_path = 'images/menu_button/sounds_on.png')

        
        
    