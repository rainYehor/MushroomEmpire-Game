import pygame
from models import *

pygame.init()



class Vilager(Graphic):         
    def __init__(self, dialog, **kwargs):
        super().__init__(**kwargs)
        self.dialog_situation = dialog
        if self.dialog_situation == "act-1":
            self.dialog_list = [
                "images/dialogs/book/page_1.png",
                "images/dialogs/book/page_2.png"
            ]
        if self.dialog_situation == "act0":
            self.dialog_list = [
                "images/dialogs/1). Початок гри/1.png",
                "images/dialogs/1). Початок гри/2.png",
                "images/dialogs/1). Початок гри/3.png",
                "images/dialogs/1). Початок гри/4.png",
                "images/dialogs/1). Початок гри/5.png",
                "images/dialogs/1). Початок гри/6.png",
                "images/dialogs/1). Початок гри/7.png",
                "images/dialogs/1). Початок гри/8.png",
                "images/dialogs/1). Початок гри/9.png"
            ]
        if self.dialog_situation == "act1":
            self.dialog_list = [
                "images/dialogs/2). Тренування/1.png",
                "images/dialogs/2). Тренування/2.png"
            ]
        if self.dialog_situation == "act2":
            self.dialog_list = [
                "images/dialogs/3). Село/1.png",
                "images/dialogs/3). Село/2.png",
                "images/dialogs/3). Село/3.png",
                "images/dialogs/3). Село/4.png",
                "images/dialogs/3). Село/5.png",
                "images/dialogs/3). Село/6.png",
                "images/dialogs/3). Село/7.png",
                "images/dialogs/3). Село/8.png",
                "images/dialogs/3). Село/9.png",
                "images/dialogs/3). Село/10.png",
                "images/dialogs/3). Село/11.png",
                "images/dialogs/3). Село/12.png",
                "images/dialogs/3). Село/13.png",
                "images/dialogs/3). Село/14.png",
                "images/dialogs/3). Село/15.png",
                "images/dialogs/3). Село/16.png"
            ]
        if self.dialog_situation == "act3":
            self.dialog_list = [
                "images/dialogs/4). За межами замку/1.png",
                "images/dialogs/4). За межами замку/2.png",
                "images/dialogs/4). За межами замку/3.png",
                "images/dialogs/4). За межами замку/4.png",
                "images/dialogs/4). За межами замку/5.png",
                "images/dialogs/4). За межами замку/6.png",
                "images/dialogs/4). За межами замку/7.png",
                "images/dialogs/4). За межами замку/8.png",
                "images/dialogs/4). За межами замку/9.png",
                "images/dialogs/4). За межами замку/10.png",
                "images/dialogs/4). За межами замку/11.png",
                "images/dialogs/4). За межами замку/12.png",
                "images/dialogs/4). За межами замку/13.png",
                "images/dialogs/4). За межами замку/14.png",
                "images/dialogs/4). За межами замку/15.png",
                "images/dialogs/4). За межами замку/16.png"
            ]
        if self.dialog_situation == "act4":
            self.dialog_list = [
                "images/dialogs/5). Магічні ліса/1.png",
                "images/dialogs/5). Магічні ліса/2.png",
                "images/dialogs/5). Магічні ліса/3.png"
            ]
        if self.dialog_situation == "act5":
            self.dialog_list = [
                "images/dialogs/5.1). Магічні ліса/4.png",
                "images/dialogs/5.1). Магічні ліса/5.png",
                "images/dialogs/5.1). Магічні ліса/6.png",
                "images/dialogs/5.1). Магічні ліса/7.png"
            ]
        if self.dialog_situation == "act6":
            self.dialog_list = [
                "images/dialogs/6). Замок принцеси/1.png",
                "images/dialogs/6). Замок принцеси/2.png",
                "images/dialogs/6). Замок принцеси/4.png",
                "images/dialogs/6). Замок принцеси/5.png",
                "images/dialogs/6). Замок принцеси/6.png",
                "images/dialogs/6). Замок принцеси/7.png"
            ]
        if self.dialog_situation == "act7":
            self.dialog_list = [
                "images/dialogs/7). Вхід до замку короля/1.png",
                "images/dialogs/7). Вхід до замку короля/2.png",
                "images/dialogs/7). Вхід до замку короля/3.png",
                "images/dialogs/7). Вхід до замку короля/4.png"
            ]
        if self.dialog_situation == "act8":
            self.dialog_list = [
                "images/dialogs/7.1). Вхід до замку короля/5.png",
                "images/dialogs/7.1). Вхід до замку короля/6.png",
                "images/dialogs/7.1). Вхід до замку короля/7.png",
                "images/dialogs/7.1). Вхід до замку короля/8.png",
                "images/dialogs/7.1). Вхід до замку короля/9.png"
            ]
        if self.dialog_situation == "act9":
            self.dialog_list = [
                "images/dialogs/8). Фінальна битва/1.png",
                "images/dialogs/8). Фінальна битва/2.png",
                "images/dialogs/8). Фінальна битва/3.png",
                "images/dialogs/8). Фінальна битва/4.png",
                "images/dialogs/8). Фінальна битва/5.png"
            ]
        if self.dialog_situation == "act11":
            self.dialog_list = [
                "images/dialogs/9). Перемога над королем/1.png",
                "images/dialogs/9). Перемога над королем/2.png",
                "images/dialogs/9). Перемога над королем/3.png",
                "images/dialogs/9). Перемога над королем/4.png",
                "images/dialogs/9). Перемога над королем/5.png",
                "images/dialogs/9). Перемога над королем/6.png",
                "images/dialogs/9). Перемога над королем/7.png"
            ]
        if self.dialog_situation == "act15":
            self.dialog_list = [
                "images/dialogs/10). Кінець/1.png",
                "images/dialogs/10). Кінець/2.png",
                "images/dialogs/10). Кінець/3.png",
                "images/dialogs/10). Кінець/4.png"
            ]
        self.dialog_counter = 0
        self.dialog_isRead = False
        self.dialog_isReaden = False
        self.text_font_1 = pygame.font.Font(None, 36)
        if self.dialog_situation == "act-1":
            self.dialog = Graphic(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, img_path=self.dialog_list[self.dialog_counter])
        else:
            self.dialog = Graphic(0, SCREEN_HEIGHT-476, SCREEN_WIDTH, 476, img_path=self.dialog_list[self.dialog_counter])
        self.darkness = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.darkness.fill((0,0,0,122))
        self.skip_button = Button(x=SCREEN_WIDTH-160, y=SCREEN_HEIGHT-60, width=160, height=60, img_path="images/menu_button/skip_button.png")
        self.was_click = False

    def check_collide(self, main_hero, keys, window, mouse_pos):
        if self.dialog_isRead:
            self.read_dialog(window, keys, mouse_pos)
        if self.rect.colliderect(main_hero):
            if self.dialog_isReaden == False and str(main_hero.dialog_readen) in self.dialog_situation:
                self.dialog_isRead = True
                main_hero.can_move = False
                

    def read_dialog(self, window, keys, mouse_pos):
        if main_hero.isAttack:
            main_hero.isAttack = False
        mouse = pygame.mouse.get_pressed()[0]
        window.blit(self.darkness, (0, 0))
        self.dialog.show_image(window)
        if (keys[pygame.K_RETURN] or mouse) and self.was_click == False:
            try:
                self.dialog_counter += 1
                if self.dialog.IMG_PATH == 'images/dialogs/4). За межами замку/15.png' or self.dialog.IMG_PATH == 'images/dialogs/6). Замок принцеси/3.png':
                    self.dialog.rect.y, self.dialog.rect.height = SCREEN_HEIGHT-476, 476 
                self.dialog.IMG_PATH = self.dialog_list[self.dialog_counter]
                if self.dialog_list[self.dialog_counter] == 'images/dialogs/4). За межами замку/15.png' or self.dialog_list[self.dialog_counter] == 'images/dialogs/6). Замок принцеси/3.png':
                    self.dialog.rect.y, self.dialog.rect.height = 0, 720 
                self.dialog.load_image()
                self.skip_reload = 60
            except IndexError:
                
                self.dialog_isRead = False
                self.dialog_isReaden = True
                main_hero.can_move = True
                main_hero.dialog_readen += 1
        if self.skip_button.check_click(mouse_pos) and mouse and self.dialog_isReaden==False:
            self.dialog_isRead = False
            self.dialog_isReaden = True
            main_hero.can_move = True
            main_hero.dialog_readen += 1
        if keys[pygame.K_RETURN] or mouse:
            self.was_click = True
        elif keys[pygame.K_RETURN] == False and mouse == False:
            self.was_click = False
        self.skip_button.show_image(window)
           