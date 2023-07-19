from models import *
from settings import *
from level_settings import *
from random import randint, choice

class Stairs(Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def check_collide(self, main_hero, keys):
        if self.rect.colliderect(main_hero):
            main_hero.climb(keys)

class Platform(Graphic):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_y = self.rect.y
        self.slide_reload = FPS*2
        self.direction = "down"
        

    def check_collide(self, main_hero, keys):
        if self.rect.collidepoint(main_hero.rect.left+main_hero.SPEED, main_hero.rect.top) or self.rect.collidepoint(main_hero.rect.right-main_hero.SPEED, main_hero.rect.top):
            coin = randint(1, 2)
            if coin == 1:
                main_hero.rect.right = self.rect.left
            if coin == 2:
                main_hero.rect.left = self.rect.right
        if self.slide_reload > 0:
            self.slide_reload -= 1
        if self.direction == "up" and self.slide_reload == 0:
            self.rect.y -= 3 
        if self.direction == "down" and self.slide_reload == 0:
            self.rect.y += 3
        if self.rect.y <= self.start_y and self.slide_reload == 0:
            self.direction = "down"
            self.slide_reload = FPS*2
        if self.rect.y > 720 - BLOCK_HEIGHT - self.rect.height and self.slide_reload == 0:
            self.direction = "up"
            self.slide_reload = FPS*2

class Chest(Graphic):
    def __init__(self, loot, **kwargs):
        super().__init__(**kwargs)
        self.loot = loot
        self.notification_time = 0
        
    def check_collide(self, main_hero, keys, window, dict):
        if self.rect.colliderect(main_hero):
            if self.notification_time == 0:
                main_hero.can_leve_underlevel = True
                main_hero.key_bool = True
                self.notification_time = 180
                dict["list_objects"].remove(self)
        if self.notification_time > 0:
            self.notification_time -= 1
            if self.notification_time == 0:
                dict["list_usable_blocks"].remove(self)
                

class LevelSign(Graphic):
    def __init__(self, teleport_x, teleport_y, direction, **kwargs):
        super().__init__(**kwargs)
        self.teleport_x = teleport_x
        self.teleport_y = teleport_y
        self.direction = direction
        self.open = False
        self.isGo = False
        self.is_selected = False
        self.standart_image = self.IMG_PATH
    def check_collide(self, main_hero, keys):
        if self.isGo == True:
            self.change_level(main_hero)
        if self.rect.colliderect(main_hero):
            if "c" not in str(self.direction):
                if type(self.direction) == int:
                    if keys[pygame.K_e]:
                        if self.isGo == False:
                            self.isGo = True
                            self.sound_counter = 0
                            main_hero.can_move = False
                    elif self.is_selected == False:
                        self.IMG_PATH = f"{self.IMG_PATH.split('.')[0]}_selected.png"
                        self.load_image()
                        self.is_selected = True
                elif main_hero.can_go_level_2:
                    if keys[pygame.K_e]:
                        if self.isGo == False:
                            self.direction = int(self.direction)
                            self.isGo = True
                            self.sound_counter = 0
                            main_hero.can_move = False
                    elif self.is_selected == False:
                        self.IMG_PATH = f"{self.IMG_PATH.split('.')[0]}_selected.png"
                        self.load_image()
                        self.is_selected = True
            else:
                if keys[pygame.K_e]:
                    if self.isGo == False and main_hero.key_bool:
                        main_hero.key_bool = False
                        self.isGo = True
                        self.sound_counter = 0
                        main_hero.can_move = False
                        #if SOUND_STATUS:
                        door_opening_sound.play()
                        self.IMG_PATH = "images/doors/door_castle_open.png"
                        self.load_image()
        else:   
            self.IMG_PATH = self.standart_image
            self.load_image()
            self.is_selected = False

    def change_level(self, main_hero):#переход в обычный левел
        if "c" not in str(self.direction) and self.isGo == True:
            if self.direction == -1:
                main_hero.forced_move("L")
            if self.direction == 1:
                main_hero.forced_move("R")
        self.sound_counter += 1
        if self.sound_counter == 100:
            main_hero.rect.x = self.teleport_x
            main_hero.rect.y = main_hero.rect.y
                
            if "c" not in str(self.direction) and self.isGo == True:
                main_hero.current_level += self.direction
            else:
                self.direction = self.direction.split("_")
                main_hero.current_level += int(self.direction[0])
            main_hero.can_move = True
            main_hero.isAttack = False
 
class Door(Graphic):
    def __init__(self, teleport_x, teleport_y, direction, **kwargs):
        self.direction = direction
        super().__init__(**kwargs)
        self.teleport_x = teleport_x
        self.teleport_y = teleport_y
        self.isGo = False
        if "out" in self.direction:
            self.lock = Graphic(self.rect.centerx - 5, self.rect.centery - 6, 10, 12, "images/hud/lock.png")
        if "under4" == self.direction or "under5" == self.direction or "under6" == self.direction or "c" in self.direction:
            self.IMG_PATH = "images/doors/door_closed.png"
            self.load_image()

    def show_image(self, window):
        if self.IMAGE != None:
            window.blit(self.IMAGE, (self.rect.x, self.rect.y))
        if "out" in self.direction and self.lock != None:
            self.lock.show_image(window)
    
    def check_collide(self, main_hero, keys):
        if self.isGo:
            if "out" in self.direction:
                self.leave_underlevel_castle(main_hero)
            else:
                self.enter_underlevel_castle(main_hero)
        if self.rect.colliderect(main_hero):
            if keys[pygame.K_e]:
                if self.direction == "out":
                    self.leave_underlevel(main_hero)
                if ("under4" == self.direction or "under5" == self.direction or "under6" == self.direction or "c" in self.direction) and self.isGo == False:
                    #if SOUND_STATUS:
                    door_opening_sound.play()
                    self.isGo = True
                    main_hero.can_move = False
                    self.sound_counter = 0
                    self.IMG_PATH = "images/doors/door_opened.png"
                    self.load_image()
                elif "under" in self.direction and self.isGo == False:
                    self.enter_underlevel(main_hero)
        if main_hero.can_leve_underlevel and self.lock != None:
            self.lock = None

    def enter_underlevel_castle(self, main_hero):
        if self.sound_counter == 100:
            self.enter_underlevel(main_hero)
            main_hero.can_move = True
        self.sound_counter += 1

    def leave_underlevel_castle(self, main_hero):
        if self.sound_counter == 100:
            self.leave_underlevel(main_hero)
            main_hero.can_move = True
            main_hero.ISinvulnerability = False
        self.sound_counter += 1

    def enter_underlevel(self, main_hero):
        main_hero.leave_x = main_hero.rect.x
        main_hero.leave_y = main_hero.rect.y
        main_hero.rect.x = self.teleport_x
        main_hero.rect.y = self.teleport_y
        main_hero.leave_level = main_hero.current_level
        main_hero.current_level = self.direction
    def leave_underlevel(self, main_hero):#"выход"
        if main_hero.can_leve_underlevel:
            main_hero.can_leve_underlevel = False
            main_hero.can_go_level_2 = True
            main_hero.rect.x, main_hero.rect.y = main_hero.leave_x, main_hero.leave_y
            main_hero.current_level = main_hero.leave_level
        

dict_objects = {
"list_objects" : [],
"list_blocks" : [],
"list_usable_blocks" : [],
"list_enemy" : []
}

def create_map(map):
    if main_hero.current_level == 5:
        under_counter = 4
        doors_img = ['images/doors/hole_left.png', 'images/doors/hole_left_prison_bad.png', 'images/doors/hole_right_prison_bad.png']
    else:
        under_counter = 1
        doors_img = ['images/doors/hole_left.png', 'images/doors/hole_left_prison_bad.png', 'images/doors/hole_right_prison_bad.png']
    dict_objects = {
    "list_objects" : [],
    "list_blocks" : [],
    "list_usable_blocks" : [],
    "list_enemy" : []
    }
    x = 0
    y = 0
    top_cordon = Graphic(x = x, y = y - BLOCK_HEIGHT, height = BLOCK_HEIGHT, width = SCREEN_WIDTH, img_path = None)
    left_cordon = Graphic(x = x - BLOCK_WIDTH, y = y - BLOCK_HEIGHT, height = SCREEN_HEIGHT, width = BLOCK_WIDTH, img_path = None)
    bottom_cordon = Graphic(x = x, y = y + SCREEN_HEIGHT, height = BLOCK_HEIGHT, width = SCREEN_WIDTH, img_path = None)
    right_cordon =  Graphic(x = x + SCREEN_WIDTH, y = y, height = SCREEN_HEIGHT, width = BLOCK_WIDTH, img_path = None)
    dict_objects["list_blocks"].append(top_cordon)
    dict_objects["list_blocks"].append(left_cordon)
    dict_objects["list_blocks"].append(bottom_cordon)
    dict_objects["list_blocks"].append(right_cordon)
    for row in map:
        for cell in row:
            if cell == '1':# - wall
                obj = Graphic(x = x, y = y,height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/blocks/block.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == '5':# - wall
                obj = Graphic(x = x, y = y,height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/blocks/castle.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == 's':# - stairs
                obj = Stairs(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/blocks/tree_ladder.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 's_c':# - stairs
                obj = Stairs(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/boss_items/normal_ladder.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'p':# - platform
                obj = Platform(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/blocks/block.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'p_c':# - platform castle
                obj = Platform(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/blocks/castle.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'c_l':# - chest left
                obj = Chest(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/items/chest_l.png', loot="key")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'c_r':# - chest left
                obj = Chest(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/items/chest_r.png', loot="key")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'e':# - enemy
                obj = Enemy(SPEED = 2, TYPE = "potruly", HP = 50, start_counter = randint(0, 19), x = x, y = y + BLOCK_HEIGHT - 70, height = 70, width = 60, img_path = "images/princess_guard_enemy/walk_r_1.png")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_enemy"].append(obj)
            if cell == 'e1':# - enemy
                obj = Enemy(SPEED = 1, TYPE = "swordman1", HP = 50, start_counter = randint(0, 100), x = x, y = y + BLOCK_HEIGHT - 100, height = 100, width = 105, img_path = "images/princess_guard_enemy/walk_r_1.png")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_enemy"].append(obj)
            if cell == 'e2':# - enemy
                obj = Enemy(SPEED = 1, TYPE = "swordman2", HP = 50, start_counter = randint(0, 100), x = x, y = y + BLOCK_HEIGHT - 100, height = 100, width = 105, img_path = "images/princess_guard_enemy/walk_r_1.png")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_enemy"].append(obj)
            if cell == 'n':# - sign to next level
                obj = LevelSign(x = x, y = y, height = 72, width = 64, img_path = f'images/signs/right_{main_hero.current_level+1}.png', teleport_x = 64, teleport_y = None, direction = 1)
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'n_all':# - sign to next level but with requirement
                obj = LevelSign(x = x, y = y, height = 72, width = 64, img_path = f'images/signs/right_{main_hero.current_level+1}.png', teleport_x = 64, teleport_y = None, direction = "1")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'n_c':# - sign to next level
                obj = LevelSign(x = x-132, y = y+BLOCK_HEIGHT - 137, height = 137, width = 115, img_path = f'images/doors/door_castle.png', teleport_x = 64, teleport_y = None, direction = "1_c")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'l':# - door to last level
                obj = LevelSign(x = x, y = y, height = 72, width = 64, img_path = f'images/signs/left_{main_hero.current_level-1}.png', teleport_x = SCREEN_WIDTH - 64*2, teleport_y = None, direction = -1)
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'u':# - door to underlevel
                if "under"+str(under_counter) in under_levels:
                    image = doors_img[0]
                    obj = Door(x = x, y = y, height = 72, width = 64, img_path = image, teleport_x = 64, teleport_y = SCREEN_HEIGHT-BLOCK_HEIGHT-main_hero.rect.height, direction = "under"+str(under_counter))
                    doors_img.remove(image)
                    dict_objects["list_objects"].append(obj)
                    dict_objects["list_usable_blocks"].append(obj)
                else:
                    doors_img.remove(doors_img[0])
                under_counter += 1
            if cell == "o":# - door from underlevel
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/doors/hole_left.png', teleport_x = 64, teleport_y = None, direction = "out")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == "o_c":# - door from underlevel
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/doors/door_closed.png', teleport_x = 64, teleport_y = None, direction = "out_c")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'm': # - dummy
                dummy = Enemy(SPEED = 0, TYPE = "dummy", HP = 100, start_counter = 0, x = x, y = y, width = 20, height = 75, img_path = 'images/items/dummy.png' )
                dict_objects["list_blocks"].append(dummy)
                dict_objects["list_objects"].append(dummy)
                dict_objects["list_enemy"].append(dummy)
            if cell == '3':
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/blocks/block_mud.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == '2':
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/blocks/block_level_2.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == 'd0':
                obj = Vilager(x = 0, y = 0, height = 720, width = 1280, img_path = None, dialog="act-1")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd1':
                obj = Vilager(x = x, y = y+BLOCK_HEIGHT-72, height = 72, width = 28, img_path = 'images/dialogs_characters/artemis_r.png', dialog="act0")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd2':
                obj = Vilager(x = x-10, y = y+BLOCK_HEIGHT-1000+BLOCK_HEIGHT, height = 1000, width = BLOCK_WIDTH, img_path = None, dialog="act1")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd3':
                obj = Vilager(x = x+BLOCK_WIDTH, y = y+BLOCK_HEIGHT-72, height = 72, width = 28, img_path = 'images/dialogs_characters/artemis_l.png', dialog="act2")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd4':
                obj = Vilager(x = x+BLOCK_WIDTH, y = y+BLOCK_HEIGHT-1000, height = 1000, width = 28, img_path = None, dialog="act3")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd5':
                obj = Vilager(x = x+BLOCK_WIDTH, y = y+BLOCK_HEIGHT-1000, height = 1000, width = 28, img_path = None, dialog="act4")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd5_1':
                obj = Vilager(x = x, y = y+BLOCK_HEIGHT-1000+BLOCK_HEIGHT, height = 1000, width = BLOCK_WIDTH, img_path = None, dialog="act5")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd6':
                obj = Vilager(x = x+10, y = y+BLOCK_HEIGHT-1000, height = 1000, width = BLOCK_WIDTH, img_path = None, dialog="act6")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd7':
                obj = Vilager(x = x+BLOCK_WIDTH, y = y+BLOCK_HEIGHT-1000, height = 1000, width = BLOCK_WIDTH, img_path = None, dialog="act7")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd7_1':
                obj = Vilager(x = x, y = y+BLOCK_HEIGHT-1000, height = 1000, width = BLOCK_WIDTH, img_path = None, dialog="act8")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd8':
                obj = Vilager(x = x, y = y+BLOCK_HEIGHT-1000, height = 1000, width = 1000, img_path = None, dialog="act9")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd9':
                obj = Vilager(x = x, y = y+BLOCK_HEIGHT, height = 1000, width = 1000, img_path = None, dialog="act11")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'd10':
                obj = Vilager(x = x, y = y+BLOCK_HEIGHT-1000, height = 1000, width = 1000, img_path = None, dialog="act15")
                dict_objects["list_objects"].append(obj)
                dict_objects["list_usable_blocks"].append(obj)
            if cell == 'h':#shop
                shop.rect.x, shop.rect.y = x, y+BLOCK_HEIGHT-200
                dict_objects["list_objects"].append(shop)
                dict_objects["list_usable_blocks"].append(shop)
            if cell == 'b':#boss
                boss = Boss(x = (SCREEN_WIDTH/2)-(190/2), y = SCREEN_HEIGHT-BLOCK_HEIGHT-150 ,  height = 150, width = 190, img_path = 'images/boss_items/boss_move/ride_l_1.png', sounds = sounds_boss)
                chandelier = Chandelier(x = boss.rect.centerx - 155, y = 0 , height = 200, width = 310, img_path = 'images/boss_items/chandelier.png')
                chandelier_holder_left = Enemy(SPEED = 0, TYPE = "chandelier_holder", HP = 4, start_counter = 0, x = chandelier.rect.left - 60, y = 0, height = 83, width = 60, img_path = 'images/boss_items/chandelier_holder_l.png')
                chandelier_holder_right = Enemy(SPEED = 0, TYPE = "chandelier_holder", HP = 4, start_counter = 0, x = chandelier.rect.right, y = 0, height = 83, width = 60, img_path = 'images/boss_items/chandelier_holder_r.png')
                dict_objects["list_objects"].append(boss)
                dict_objects["list_blocks"].append(boss)
                dict_objects["list_objects"].append(chandelier)
                dict_objects["list_blocks"].append(chandelier)
                dict_objects["chandelier"] = chandelier
                dict_objects["list_objects"].append(chandelier_holder_left)
                dict_objects["list_blocks"].append(chandelier_holder_left)
                dict_objects["list_enemy"].append(chandelier_holder_left)

                dict_objects["list_objects"].append(chandelier_holder_right)
                dict_objects["list_blocks"].append(chandelier_holder_right)
                dict_objects["list_enemy"].append(chandelier_holder_right)
                dict_objects["boss"] = boss
            x += BLOCK_WIDTH
        x = 0   
        y += BLOCK_HEIGHT
    dict_objects["list_objects"].append(main_hero)
    return dict_objects