import pygame, math
from graphic import Graphic
from random import randint
from sounds import sounds_boss
class BossBullet(Graphic):
    def __init__(self, speed, main_hero_pos, **kwargs):
        super().__init__(**kwargs)
        self.angle = math.atan2(main_hero_pos[1]-self.rect.y, main_hero_pos[0]-self.rect.x)
        self.angle_degrease = int(self.angle*180/math.pi)
        self.speed = speed
        self.destination_x = math.cos(self.angle)*self.speed
        self.destination_y = math.sin(self.angle)*self.speed
        self.IMG_PATH = "images/boss_items/bullet.png"
        self.load_image()

    def load_image(self):
        self.IMAGE = pygame.image.load(self.IMG_PATH)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.rect.width, self.rect.height))
        self.IMAGE = pygame.transform.rotate(self.IMAGE, -self.angle_degrease)

    def update(self, screen):
        self.rect.x += self.destination_x
        self.rect.y += self.destination_y
        screen.blit(self.IMAGE, (self.rect.x, self.rect.y))

    def check_collide(self, main_hero_rect, main_hero_hp):
        if self.rect.colliderect(main_hero_rect):
            main_hero_hp -= 2
        return main_hero_hp

class Boss(Graphic):
    def __init__(self, sounds, **kwargs):
        super().__init__(**kwargs)
        self.isAlive = True
        self.bullet_list = []
        self.reload_counter = 60
        self.position = "center"
        self.center_position_x = self.rect.x
        self.left_position_x = self.rect.x - 300
        self.right_position_x = self.rect.x + 300
        self.step = None
        self.move_reload = 180
        self.angle = 20
        self.door = Graphic(self.rect.centerx-64, self.rect.bottom-144, 128, 144, img_path=None)
        self.animation_move_counter = 0
        self.sound_reload = 0
        self.sounds = sounds
        self.look = "L"

        self.list_stay_left = [
            "images/boss_items/boss_move/stay_l_0.png",
            "images/boss_items/boss_move/stay_l_1.png"
        ]

        self.list_stay_right = [
            "images/boss_items/boss_move/stay_r_0.png",
            "images/boss_items/boss_move/stay_r_1.png"
        ]

        self.list_move_left = [
            "images/boss_items/boss_move/ride_l_1.png",
            "images/boss_items/boss_move/ride_l_2.png",
            "images/boss_items/boss_move/ride_l_3.png",
            "images/boss_items/boss_move/ride_l_4.png",
            "images/boss_items/boss_move/ride_l_5.png",
            "images/boss_items/boss_move/ride_l_6.png",
            "images/boss_items/boss_move/ride_l_7.png"
        ]
        self.list_move_right = [
            "images/boss_items/boss_move/ride_r_1.png",
            "images/boss_items/boss_move/ride_r_2.png",
            "images/boss_items/boss_move/ride_r_3.png",
            "images/boss_items/boss_move/ride_r_4.png",
            "images/boss_items/boss_move/ride_r_5.png",
            "images/boss_items/boss_move/ride_r_6.png",
            "images/boss_items/boss_move/ride_r_7.png"
        ]


    def animation_move(self):
        self.animation_move_counter += 1
        if self.animation_move_counter == 70:
            self.animation_move_counter = 0
        if self.position == "going_right":
            self.IMG_PATH =  self.list_move_right[self.animation_move_counter//10]
            self.load_image()
        if self.position == "going_left":
            self.IMG_PATH =  self.list_move_left[self.animation_move_counter//10]
            self.load_image()
        if self.position == "center":
            if self.look == "L":
                if self.animation_move_counter >= 20:
                    self.animation_move_counter = 0
                self.IMG_PATH =  self.list_stay_left[self.animation_move_counter//10]
                self.load_image()
            if self.look == "R":
                if self.animation_move_counter >= 20:
                    self.animation_move_counter = 0
                self.IMG_PATH =  self.list_stay_right[self.animation_move_counter//10]
                self.load_image()
        if self.position == "left":
            if self.look == "L":
                if self.animation_move_counter >= 20:
                    self.animation_move_counter = 0
                self.IMG_PATH =  self.list_stay_left[self.animation_move_counter//10]
                self.load_image()
            if self.look == "R":
                if self.animation_move_counter >= 20:
                    self.animation_move_counter = 0
                self.IMG_PATH =  self.list_stay_right[self.animation_move_counter//10]
                self.load_image()
        if self.position == "right":
            if self.look == "L":
                if self.animation_move_counter >= 20:
                    self.animation_move_counter = 0
                self.IMG_PATH =  self.list_stay_left[self.animation_move_counter//10]
                self.load_image()
            if self.look == "R":
                if self.animation_move_counter >= 20:
                    self.animation_move_counter = 0
                self.IMG_PATH =  self.list_stay_right[self.animation_move_counter//10]
                self.load_image()


    def death(self, window, main_hero):
        self.rect.y+=1
        self.door.show_image(window)
        if self.door.rect.colliderect(main_hero.rect) and main_hero.dialog_readen != 15:
            main_hero.dialog_readen = 15

    def shoot(self, main_hero, window):
        if self.isAlive == False:
            self.death(window, main_hero)
            if main_hero.dialog_readen < 11:
                main_hero.dialog_readen = 11
        else:
            if self.reload_counter==0:
                #if SOUND_STATUS:
                self.sounds["boss_shoot"].play()
                bullet = BossBullet(x=self.rect.centerx, y=self.rect.centery, width=75, height=40, img_path=None, speed=20, main_hero_pos=main_hero.rect.center)
                self.bullet_list.append(bullet)
                self.reload_counter = 160
            else:
                self.reload_counter -= 1

    def move(self):
        if self.isAlive == False:
            pass
        else:
            #if SOUND_STATUS:
            if self.sound_reload == 0:
                self.sounds["boss_ride"].play()
                self.sound_reload = 78*60
            else:
                self.sound_reload -= 1
            self.animation_move()
            if self.position == "center":
                if self.move_reload == 0:
                    coin = randint(1, 2)
                    if coin == 1:
                        self.position = "going_left"
                        self.step = (self.left_position_x - self.rect.x)/180
                        self.look = "L"
                    if coin == 2:
                        self.position = "going_right"
                        self.step = (self.right_position_x - self.rect.x)/180
                        self.look = "R"
                else:
                    self.move_reload -= 1
            if self.position == "left":
                if self.move_reload == 0:
                    coin = randint(1, 2)
                    if coin == 1:
                        self.position = "going_center"
                        self.step = (self.center_position_x - self.rect.x)/180
                        self.look = "R"
                    if coin == 2:
                        self.position = "going_right"
                        self.step = (self.right_position_x - self.rect.x)/180
                        self.look = "R"
                else:
                    self.move_reload -= 1
            if self.position == "right":
                if self.move_reload == 0:
                    coin = randint(1, 2)
                    if coin == 1:
                        self.position = "going_center"
                        self.step = (self.center_position_x - self.rect.x)/180
                        self.look = "L"
                    if coin == 2:
                        self.position = "going_left"
                        self.step = (self.left_position_x - self.rect.x)/180
                        self.look = "L"
                else:
                    self.move_reload -= 1
            if self.position == "going_left":
                if self.rect.x != self.left_position_x:
                    self.rect.x += self.step
                else:
                    self.position = "left"
                    self.move_reload = 180
            if self.position == "going_right":
                if self.rect.x != self.right_position_x:
                    self.rect.x += self.step
                else:
                    self.position = "right"
                    self.move_reload = 180
            if self.position == "going_center":
                if self.rect.x != self.center_position_x:
                    self.rect.x += self.step
                else:
                    self.position = "center"
                    self.move_reload = 300

class Chandelier(Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def check_chandelier(self, chandelier_holder_list, boss):
        if len(chandelier_holder_list) == 0:
            self.rect.y += 20
            if self.rect.colliderect(boss.rect) and boss.isAlive:
                boss.isAlive = False
                boss.door.IMG_PATH = 'images/doors/door_castle.png'
                boss.door.load_image()


