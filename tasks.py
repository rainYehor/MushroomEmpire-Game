import pygame 
from models import *

class Task_menu(Graphic):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.CURRENT_TASK = None
        self.font = pygame.font.Font(None, 26)
        self.font1 = pygame.font.Font(None, 16)
    def create_task(self,name,description,window):
        end = 48
        task_name = self.font.render(name, True, (0,0,0))
        if end > 1:
            words = []
            for i in description:
                words.append(i)
                if len(words) % end == 0:
                    words.append('-')
            description = "".join(words)
            list_words = description.split('-')
            list_length = len(list_words)
            i = 0
            yy = i
            counter = 0
            for i in range(0, list_length):
                j = i + 1
                y_i = self.rect.y * j
                task_description = self.font1.render(list_words[i], True, (0,0,0))
                if i == yy+1: 
                    window.blit(task_description,(self.rect.x+3,y_i+70+counter*16))
                else:
                    window.blit(task_description,(self.rect.x+3,y_i+70))
                yy = i
                counter += 1
        else:
            window.blit(text, (self.rect.x+3,self.rect.y+70))

        window.blit(task_name,(self.rect.x+3,self.rect.y+40))

        

tsk_menu = Task_menu(x = SCREEN_WIDTH-300, y = 0, width = 300, height = 120, img_path = 'images/hud/task_panel.png')