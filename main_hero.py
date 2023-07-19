import pygame
from models import *
from sounds import sounds_main_hero



class Main_hero(Graphic):
    def __init__(self, SPEED, sounds, **kwargs):
        super().__init__(**kwargs)
        self.current_level = 1
        self.HP = 10
        self.new_HP = 10
        self.damage = 5
        self.main_hero_looks = 'R'
        self.SPEED = SPEED
        self.gravity_active = False
        self.jump_distance = 130
        self.isJump = False
        self.can_move = True
        self.isAttack = False
        self.ISinvulnerability = False
        self.climb_was = False
        self.isClimb = False
        
        self.font = pygame.font.Font(None, 30)
        self.health = Graphic(x = 0, y = 0, width = 200, height = 44, img_path = 'images/hud/hp_1.png')
        self.money_count = 150

        self.dialog_readen = -1

        self.money_panel = Graphic(x = 0, y = 50, width = 50, height = 66, img_path = "images/hud/coin_bag_1.png")
        self.money_count_position = (self.money_panel.rect.centerx-self.money_panel.rect.width/4, self.money_panel.rect.centery - (self.font.get_height()/2))
        self.money_add = Graphic(x = self.money_panel.rect.right, y = self.money_panel.rect.y, width = 95, height = 66, img_path = "images/hud/coin_1.png")
        self.money_add_list = [
            'images/hud/coin_1.png',
            'images/hud/coin_2.png',
            'images/hud/coin_3.png',
            'images/hud/coin_4.png'
        ]
        self.money_add_counter = 120
        self.key = Graphic(x = self.money_panel.rect.left, y = self.money_panel.rect.bottom, width = 100, height = 50, img_path = "images/hud/key.png")
        self.key_bool = False

        self.armor_indicators = [
            Graphic(x = self.health.rect.right, y = self.health.rect.centery - 16, width = 27, height = 32, img_path = "images/hud/shield_icon.png"),
            Graphic(x = self.health.rect.right+30, y = self.health.rect.centery - 16, width = 27, height = 32, img_path = "images/hud/shield_icon.png"),
            Graphic(x = self.health.rect.right+30+30, y = self.health.rect.centery - 16, width = 27, height = 32, img_path = "images/hud/shield_icon.png"),
            Graphic(x = self.health.rect.right+30+30+30, y = self.health.rect.centery - 16, width = 27, height = 32, img_path = "images/hud/shield_icon.png"),
            Graphic(x = self.health.rect.right+30+30+30+30, y = self.health.rect.centery - 16, width = 27, height = 32, img_path = "images/hud/shield_icon.png"),
            Graphic(x = self.health.rect.right+30+30+30+30+30, y = self.health.rect.centery - 16, width = 27, height = 32, img_path = "images/hud/shield_icon.png")
        ]
        self.armor = 0

        self.invulnerability_counter = 0
        self.walk_counter = 0
        self.attack_counter = 0
        self.climb_counter = 0
        
        self.left_hit = Graphic(0,0,50,50, None)
        self.right_hit = Graphic(0,0,50,50, None)
        self.hits = [self.left_hit, self.right_hit]

        self.can_leve_underlevel = False
        self.can_go_level_2 = False

        self.leave_x = None
        self.leave_y = None
        self.leave_level = None

        self.img_rect = pygame.Rect(0,0,64,68)

        self.list_walk_right = [
    'images/gribori/damage10/walk_r_1.png',
    'images/gribori/damage10/walk_r_2.png',
    'images/gribori/damage10/walk_r_3.png',
    'images/gribori/damage10/walk_r_4.png',
    'images/gribori/damage10/stay_r.png'
] 
        self.list_walk_left = [
    'images/gribori/damage10/walk_l_1.png',
    'images/gribori/damage10/walk_l_2.png',
    'images/gribori/damage10/walk_l_3.png',
    'images/gribori/damage10/walk_l_4.png',
    'images/gribori/damage10/stay_l.png'
]
        self.list_attack_right = [
    'images/gribori/damage10/attack_r_1.png',
    'images/gribori/damage10/attack_r_2.png',
    'images/gribori/damage10/attack_r_3.png',
    'images/gribori/damage10/attack_r_4.png',
    'images/gribori/damage10/attack_r_5.png'
]
        self.list_attack_left = [
    'images/gribori/damage10/attack_l_1.png',
    'images/gribori/damage10/attack_l_2.png',
    'images/gribori/damage10/attack_l_3.png',
    'images/gribori/damage10/attack_l_4.png',
    'images/gribori/damage10/attack_l_5.png'
]
        
        self.list_health = [
    'images/hud/hp_11.png',
    'images/hud/hp_10.png',
    'images/hud/hp_9.png',
    'images/hud/hp_8.png',
    'images/hud/hp_7.png',
    'images/hud/hp_6.png',
    'images/hud/hp_5.png',
    'images/hud/hp_4.png',
    'images/hud/hp_3.png',
    'images/hud/hp_2.png',
    'images/hud/hp_1.png'
]
        self.list_climb = [
    'images/gribori/damage10/climb_1.png',
    'images/gribori/damage10/climb_2.png'
        ]

        self.list_effect = [
    'images/gribori/damage10/attack_effect_1.png',
    'images/gribori/damage10/attack_effect_2.png',
    'images/gribori/damage10/attack_effect_3.png',
    'images/gribori/damage10/attack_effect_4.png'
        ]

        self.sounds = sounds
#    def test_death(self):
#        keys = pygame.key.get_pressed()
#        if keys[pygame.K_l]:
#            self.HP -= 10
#            print(self.HP)

         

    def load_image(self):
        self.IMAGE = pygame.image.load(self.IMG_PATH)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (64,68))
    
    def show_image(self, window):
        self.img_rect.center = self.rect.center
        if self.IMAGE != None:
            window.blit(self.IMAGE, (self.img_rect.x, self.img_rect.y))

    def death_check(self):
        if self.HP <= 0:
            scene = "death" 
            return scene        

    def bars(self, window):
        self.health.show_image(window)
        self.money_panel.show_image(window)
        if main_hero.key_bool:
            self.key.show_image(window)
        self.text = self.font.render(str(self.money_count), True, (0,0,0))
        window.blit(self.text, self.money_count_position)
        if self.money_add_counter < 20*2:
            self.money_add.IMG_PATH = self.money_add_list[self.money_add_counter//10]
            self.money_add.load_image()
            self.money_add.show_image(window)
            self.money_add_counter += 1
        if self.armor > 0:
            for i in range(self.armor):
                self.armor_indicators[i].show_image(window)

        
    def change_images(self):
        self.list_walk_right = [f"{img.split('/')[0]}/{img.split('/')[1]}/damage{self.HP}/{img.split('/')[3]}" for img in self.list_walk_right]
        self.list_walk_left = [f"{img.split('/')[0]}/{img.split('/')[1]}/damage{self.HP}/{img.split('/')[3]}" for img in self.list_walk_left]
        self.list_attack_right = [f"{img.split('/')[0]}/{img.split('/')[1]}/damage{self.HP}/{img.split('/')[3]}" for img in self.list_attack_right]
        self.list_attack_left = [f"{img.split('/')[0]}/{img.split('/')[1]}/damage{self.HP}/{img.split('/')[3]}" for img in self.list_attack_left]
        self.list_climb = [f"{img.split('/')[0]}/{img.split('/')[1]}/damage{self.HP}/{img.split('/')[3]}" for img in self.list_climb]

    def change_health_bar(self):
        if self.HP > self.new_HP and self.ISinvulnerability == False:
            if self.armor > 0:
                self.armor - 1
                self.ISinvulnerability = True
            else:
                self.HP = self.new_HP
                self.health.IMG_PATH = self.list_health[self.HP // 1]
                self.health.load_image()
                self.ISinvulnerability = True
                self.change_images()
        elif self.HP < self.new_HP:
            if self.new_HP > 10:
                self.new_HP, self.HP = 10, 10
            else:
                self.HP = self.new_HP
            self.health.IMG_PATH = self.list_health[self.HP // 1]
            self.health.load_image()
            self.change_images()

        

    def check_earn_damage(self):
        self.change_health_bar()
        if self.ISinvulnerability:
            self.isAttack = False
            self.invulnerability_counter += 1
            if self.invulnerability_counter >= 80:
                self.ISinvulnerability = False
                self.invulnerability_counter = 0
            if self.invulnerability_counter == 1:
                if self.main_hero_looks == "R":
                    self.IMG_PATH = "images/gribori/damage10/gribori_hurted_r.png"
                    self.load_image()
                if self.main_hero_looks == "L":
                    self.IMG_PATH = "images/gribori/damage10/gribori_hurted_l.png"
                    self.load_image()


    def animation_climb(self):
        if self.ISinvulnerability == False:
            self.isClimb = True
            if self.climb_counter < 40 and self.climb_counter % 5 == 0:#
                self.IMG_PATH = self.list_climb[self.climb_counter//20]
                self.load_image()
            elif self.climb_counter >= 40:
                self.climb_counter = -1
            self.climb_counter += 1

    def animation_walk(self):
        if self.ISinvulnerability == False and self.isClimb == False:
            if self.walk_counter % 8 == 0 and self.walk_counter > 0:
                #if SOUND_STATUS:
                self.sounds["walk_grass_sound"].play()
            if self.main_hero_looks == 'R':
                if self.walk_counter == -1:
                    self.IMG_PATH = self.list_walk_right[-1]
                    self.load_image()
                elif self.walk_counter < 20 and (self.walk_counter % 5) == 0:#
                    self.IMG_PATH = self.list_walk_right[self.walk_counter//5]
                    self.load_image()
                elif self.walk_counter >= 20:
                    self.walk_counter = -1
            if self.main_hero_looks == 'L':
                if self.walk_counter == -1:
                    self.IMG_PATH = self.list_walk_left[-1]
                    self.load_image()
                elif self.walk_counter < 20 and self.walk_counter % 5 == 0:#
                    self.IMG_PATH = self.list_walk_left[self.walk_counter//5]
                    self.load_image()
                elif self.walk_counter >= 20:
                    self.walk_counter = -1
            self.walk_counter += 1

    def animation_attack(self):
        if self.ISinvulnerability == False and self.isClimb == False:
            if self.attack_counter == 10:
                #if SOUND_STATUS:
                self.sounds["attack_sound"].play()
            if self.main_hero_looks == 'R':
                if self.attack_counter < 15 and self.attack_counter % 3 == 0:#
                    self.IMG_PATH = self.list_attack_right[self.attack_counter//3]
                    self.load_image()
                if self.attack_counter >= 15:
                    self.isAttack = False
                    self.attack_counter = 0
            if self.main_hero_looks == 'L':
                if self.attack_counter < 15 and self.attack_counter % 3 == 0:#
                    self.IMG_PATH = self.list_attack_left[self.attack_counter//3]
                    self.load_image()
                if self.attack_counter >= 15:
                    self.isAttack = False
                    self.attack_counter = 0
            self.attack_counter += 1
    def climb(self, keys):
        if self.ISinvulnerability == False:
            if keys[pygame.K_w] and self.climb_was == False:
                main_hero.climb_up()
                self.climb_was = True
            if keys[pygame.K_s] and self.climb_was == False:
                main_hero.climb_down()
                self.climb_was = True
            if keys[pygame.K_w] == False and keys[pygame.K_s] == False and self.climb_was == False and self.gravity_active==True:
                main_hero.climb_stay()
                self.climb_was = True

    def climb_up(self):
        self.gravity_active = False
        self.rect.y -= self.SPEED/2
        self.animation_climb()
    def climb_down(self):
        self.gravity_active = False
        self.rect.y += self.SPEED/1.5
        self.animation_climb()
    def climb_stay(self):
        self.gravity_active = False
        self.isClimb = True
        if self.IMG_PATH != self.list_climb[0] and self.IMG_PATH != self.list_climb[1]:
            self.IMG_PATH = self.list_climb[0]
            self.load_image()


    def collision(self, list_blocks):
        for block in list_blocks:            
            if self.rect.colliderect(block.rect):
                if self.rect.right >= block.rect.left and self.rect.right <= block.rect.left + self.SPEED:
                    self.rect.right = block.rect.left - 1
                if self.rect.left <= block.rect.right and self.rect.left >= block.rect.right - self.SPEED*2:
                    self.rect.left = block.rect.right + 1
                if self.rect.top <= block.rect.bottom and self.rect.top >= block.rect.bottom - self.SPEED*4:
                    self.rect.top = block.rect.bottom
                if self.rect.bottom >= block.rect.top and self.rect.bottom <= block.rect.top + self.SPEED*4:
                    self.rect.bottom = block.rect.top
                    #self.gravity_active = False
                    self.jump_distance = 130
                    self.isJump = False
            if block.rect.collidepoint(self.rect.x, self.rect.bottom + 1):
                    self.gravity_active = False

    def forced_move(self, side):
        if self.can_move == False:
            if side == "L":
                self.main_hero_looks = 'L'
                self.rect.x -= self.SPEED/2.5
                self.animation_walk()
            if side == "R":
                self.main_hero_looks = 'R'
                self.rect.x += self.SPEED/2.5
                self.animation_walk()

    def move(self, list_blocks):
        if self.can_move:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.gravity_active == False:
                self.isJump = True
                self.gravity_active = False


            if self.isJump == True and self.isClimb == False:
                self.rect.y -= self.SPEED*4
                self.jump_distance -= self.SPEED*4
                if self.jump_distance <= 0:
                    self.isJump = False
                    self.gravity_active = True
                    self.jump_distance = 130


            if keys[pygame.K_a]:
                if self.isAttack == False:
                    self.main_hero_looks = 'L'
                self.rect.x -= self.SPEED
                if self.ISinvulnerability == False and self.isAttack == False:
                    self.animation_walk()
            if keys[pygame.K_d]:
                if self.isAttack == False:
                    self.main_hero_looks = 'R'
                self.rect.x += self.SPEED
                if self.ISinvulnerability == False and self.isAttack == False:
                    self.animation_walk()

            if keys[pygame.K_a] == False and keys[pygame.K_d] == False and self.isAttack == False and self.isClimb == False:
                self.walk_counter = -1
                if self.ISinvulnerability == False:
                    self.animation_walk()
            #Гравитация
            if self.gravity_active == True:
                self.rect.y += self.SPEED
            self.gravity_active = True
            self.isClimb = False
            self.climb_was = False
            self.collision(list_blocks)

    def attack(self):
        if self.can_move == True and self.isClimb == False:
            mouse = pygame.mouse.get_pressed()[0]

            if mouse or self.isAttack:
                self.isAttack = True
                self.animation_attack()
                if self.attack_counter == 11:
                    if self.main_hero_looks == 'R':
                        self.right_hit.rect.left, self.right_hit.rect.y = self.rect.right + 10, self.rect.y
                    if self.main_hero_looks == 'L':
                        self.left_hit.rect.right, self.left_hit.rect.y = self.rect.left - 10, self.rect.y
                else:
                    self.right_hit.IMG_PATH, self.left_hit.IMG_PATH = None, None
                    self.right_hit.rect.x, self.right_hit.rect.y = 0, 0
                    self.left_hit.rect.x, self.left_hit.rect.y = 0, 0
    def receive_money(self, ammount):
        self.money_count += ammount
        self.change_coin_bag()
        self.money_add_counter = 0

    def change_coin_bag(self):
        if self.money_count < 150:
            self.money_panel.IMG_PATH = "images/hud/coin_bag_0.png"
            self.money_panel.load_image()
        if self.money_count >= 150 and self.money_count < 300:
            self.money_panel.IMG_PATH = "images/hud/coin_bag_1.png"
            self.money_panel.load_image()
        if self.money_count >= 300 and self.money_count < 500:
            self.money_panel.IMG_PATH = "images/hud/coin_bag_2.png"
            self.money_panel.load_image()
        if self.money_count >= 500:
            self.money_panel.IMG_PATH = "images/hud/coin_bag_3.png"
            self.money_panel.load_image()
        
main_hero = Main_hero(SPEED = 5, x = 700, y = 720-68-36, width = 20, height = 68, img_path = 'images/gribori/damage10/stay_r.png', sounds = sounds_main_hero)