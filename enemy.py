import pygame
from random import randint, choice
from models import Graphic, levels
pygame.init()
dummy_dialog_1 = {
    0 : "Привіт!",
    1 : "Я звичайний манекен!",
    2 : "Так, і я говорю!",
    3 : "Якісь питання?"
}
class Enemy(Graphic):
    def __init__(self, SPEED, TYPE, HP, start_counter, **kwargs):
        super().__init__(**kwargs)
        self.SPEED = SPEED
        self.TYPE = TYPE
        self.HP = HP
        self.enemy_move_counter = start_counter
        self.enemy_animation_counter = 0
        self.earning_damage = 0
        self.image_hit = Graphic(0, 0, 0, 0, None)
        self.vision = None
        if TYPE == "dummy" or TYPE == "potruly" or TYPE == "swordman1" or TYPE == "swordman2":
            self.font = pygame.font.Font(None, 36)

        if TYPE == "potruly":
            self.animation_walk_l_list = [
                "images/grey_shroom/walk_l_1.png",
                "images/grey_shroom/walk_l_2.png",
                "images/grey_shroom/walk_l_3.png",
                "images/grey_shroom/walk_l_4.png"
            ]
            self.animation_walk_r_list = [
                "images/grey_shroom/walk_r_1.png",
                "images/grey_shroom/walk_r_2.png",
                "images/grey_shroom/walk_r_3.png",
                "images/grey_shroom/walk_r_4.png"
            ]
            self.stay_r_image = "images/grey_shroom/stay_r.png"
            self.stay_l_image = "images/grey_shroom/stay_l.png"
            self.side = "R"
        if "swordman" in TYPE:
            self.isChase = False
            self.start_position = self.rect.x
            self.returning = False
            self.side = "R"
            if "1" in TYPE:
                self.animation_walk_l_list = [
                    "images/princess_guard_enemy/walk_l_1.png",
                    "images/princess_guard_enemy/walk_l_2.png",
                    "images/princess_guard_enemy/walk_l_3.png",
                    "images/princess_guard_enemy/walk_l_4.png"
                ]
                self.animation_walk_r_list = [
                    "images/princess_guard_enemy/walk_r_1.png",
                    "images/princess_guard_enemy/walk_r_2.png",
                    "images/princess_guard_enemy/walk_r_3.png",
                    "images/princess_guard_enemy/walk_r_4.png"
                ]
                self.stay_r_image = "images/princess_guard_enemy/stay_r.png"
                self.stay_l_image = "images/princess_guard_enemy/stay_l.png"
            elif "2" in TYPE:
                self.HP *= 3
                self.animation_walk_l_list = [
                    "images/castle_guard_enemy/walk_l_1.png",
                    "images/castle_guard_enemy/walk_l_2.png",
                    "images/castle_guard_enemy/walk_l_3.png",
                    "images/castle_guard_enemy/walk_l_4.png"
                ]
                self.animation_walk_r_list = [
                    "images/castle_guard_enemy/walk_r_1.png",
                    "images/castle_guard_enemy/walk_r_2.png",
                    "images/castle_guard_enemy/walk_r_3.png",
                    "images/castle_guard_enemy/walk_r_4.png"
                ]
                self.stay_r_image = "images/castle_guard_enemy/stay_r.png"
                self.stay_l_image = "images/castle_guard_enemy/stay_l.png"
        self.phrase_counter = 0

    def change_side(self):
        if self.side == "R":
            self.side = "L"
        elif self.side == "L":
            self.side = "R" 
    def show_hp(self, window):
        self.text = self.font.render(f"{self.HP}", True, (0,0,0))
        window.blit(self.text, (self.rect.right - (self.text.get_size()[0] / 2), self.rect.top - (self.text.get_size()[1] / 2)))

    def act(self, window, main_hero):
        if self.TYPE == "dummy":
            self.act_dummy(window, main_hero.hits, main_hero.list_effect, main_hero.damage)
        if self.TYPE == "potruly":
            main_hero.new_HP = self.act_potruly(window, main_hero.hits, main_hero.damage, main_hero.rect, main_hero.HP, main_hero.list_effect)
            if self.HP <= 0:
                main_hero.receive_money(randint(45, 70))
        if self.TYPE == "swordman1" or self.TYPE == "swordman2":
            if self.vision == None:
                self.vision = Graphic(self.rect.x, self.rect.y, 400, self.rect.height, img_path=None)
            main_hero.new_HP = self.act_swordman(window, main_hero.hits, main_hero.damage, main_hero.rect, main_hero.HP, main_hero.list_effect)
            if self.HP <= 0:
                main_hero.receive_money(randint(160, 200))
        return main_hero

    def check_earn_damage(self, window, hits, damage, list_effect):
        for hit in hits:
            if self.earning_damage > 0:
                self.image_hit.rect.center = self.rect.center
                self.image_hit.show_image(window)
                self.earning_damage -= 1
            if hit.rect.colliderect(self.rect):
                self.HP -= damage
                hit.rect.center = self.rect.center
                hit.IMG_PATH = choice(list_effect)
                hit.load_image()
                hit.show_image(window)
                self.image_hit = Graphic(hit.rect.x, hit.rect.y, hit.rect.width, hit.rect.height, img_path=hit.IMG_PATH)
                self.earning_damage = 10


    def act_dummy(self, window, hits, list_effect, damage):
        self.check_earn_damage(window, hits, damage, list_effect)
        self.phrase_counter += 1
        if self.phrase_counter >= 720:
            self.phrase_counter = 0
        if self.HP == 100:
            self.phrase = dummy_dialog_1[self.phrase_counter // 180]
        else:
            self.phrase = f"Ауч, як боляче!"
        self.text = self.font.render(self.phrase, True, (0,0,0))
        window.blit(self.text, (self.rect.centerx - (self.text.get_size()[0] / 2), self.rect.top - (self.text.get_size()[1] / 2)))
    
    def act_potruly(self, window, hits, damage, main_hero_rect, main_hero_hp, list_effect):
        self.potruly_move()
        self.potruly_animation()
        self.check_earn_damage(window, hits, damage, list_effect)
        if self.rect.colliderect(main_hero_rect):
            main_hero_hp -= 1
        self.show_hp(window)
        return main_hero_hp

    def act_chandelier_holder(self, hits, boss_pos):
        for hit in hits:
            if hit.rect.colliderect(self.rect) and (boss_pos == "center" or boss_pos == "going_center"):
                self.HP -= 1

    def act_swordman(self, window, hits, damage, main_hero_rect, main_hero_hp, list_effect):
        if self.vision.rect.colliderect(main_hero_rect) and self.isChase == False:
            self.isChase = True
            self.start_position = self.rect.x
            self.chasing_x = main_hero_rect.x
            self.side = self.chasing_x - self.rect.x
            self.vision.rect.x, self.vision.rect.y = 0, 0
            if self.side < 0:
                self.side = "L"
                self.SPEED *= 3
            else:
                self.side = "R"
                self.SPEED *= 3
        if self.isChase:
            self.swordman_chasing()
        elif self.isChase == False:
            self.swordman_move()
        if self.rect.colliderect(main_hero_rect):
            main_hero_hp -= 1
        self.swordman_animation()
        self.check_earn_damage(window, hits, damage, list_effect)

        self.show_hp(window)
        return main_hero_hp

    def potruly_move(self):
        if self.enemy_move_counter < 300-140:
            if self.side == "R":
                self.rect.x += self.SPEED
            if self.side == "L":
                self.rect.x -= self.SPEED
        if self.enemy_move_counter >= 300-140 and self.enemy_move_counter < 300:
            pass
        if self.enemy_move_counter >= 300:
            self.enemy_move_counter = 0
            self.change_side()
        self.enemy_move_counter += 1

    def potruly_animation(self):
        if self.enemy_animation_counter < 10*4 and (self.enemy_animation_counter % 10) == 0 and self.enemy_move_counter < 300-140:
            if self.side == "L":
                self.IMG_PATH = self.animation_walk_l_list[self.enemy_animation_counter//10]
                self.load_image()
            if self.side == "R":
                self.IMG_PATH = self.animation_walk_r_list[self.enemy_animation_counter//10]
                self.load_image()
        elif self.enemy_move_counter == 300-140:
            if self.side == "R":
                self.IMG_PATH = self.stay_r_image
                self.load_image()
            if self.side == "L":
                self.IMG_PATH = self.stay_l_image
                self.load_image()
        elif self.enemy_animation_counter >= 10*4:
            self.enemy_animation_counter = -1
        self.enemy_animation_counter += 1

    def swordman_move(self):
        if self.enemy_move_counter < 200-40:
            if self.side == "R":
                self.rect.x += self.SPEED
                self.vision.rect.left, self.vision.rect.y = self.rect.right, self.rect.y
            if self.side == "L":
                self.rect.x -= self.SPEED
                self.vision.rect.right, self.vision.rect.y = self.rect.left, self.rect.y
        if self.enemy_move_counter >= 200-40 and self.enemy_move_counter < 200:
            pass
        if self.enemy_move_counter >= 200:
            self.enemy_move_counter = 0
            self.change_side()
        self.enemy_move_counter += 1
                
    def swordman_chasing(self):
        if self.rect.collidepoint(self.chasing_x, self.rect.y) and self.returning == False:
            self.SPEED /= 3
            self.returning = True
        if self.returning:
            if self.rect.collidepoint(self.start_position, self.rect.y):
                self.isChase = False
                self.returning = False
            else:
                if self.side == "R":
                    self.rect.x -= self.SPEED
                if self.side == "L":
                    self.rect.x += self.SPEED
        if self.side == "R" and self.returning == False:
            self.rect.x += self.SPEED
        if self.side == "L" and self.returning == False:
            self.rect.x -= self.SPEED

    def swordman_animation(self):
        if self.isChase:
            if self.returning:
                if self.enemy_animation_counter < 10*4 and (self.enemy_animation_counter % 10) == 0:
                    if self.side == "L":
                        self.IMG_PATH = self.animation_walk_r_list[self.enemy_animation_counter//10]
                        self.load_image()
                    if self.side == "R":
                        self.IMG_PATH = self.animation_walk_l_list[self.enemy_animation_counter//10]
                        self.load_image()
                elif self.enemy_animation_counter >= 10*4:
                    self.enemy_animation_counter = 0
            else:
                if self.enemy_animation_counter < 3*4 and (self.enemy_animation_counter % 3) == 0:
                    if self.side == "R":
                        self.IMG_PATH = self.animation_walk_r_list[self.enemy_animation_counter//3]
                        self.load_image()
                    if self.side == "L":
                        self.IMG_PATH = self.animation_walk_l_list[self.enemy_animation_counter//3]
                        self.load_image()
                elif self.enemy_animation_counter >= 3*4:
                    self.enemy_animation_counter = -1
        else:
            if self.enemy_move_counter == 200-40 and self.enemy_move_counter < 200:
                if self.side == "R":
                    self.IMG_PATH = self.stay_r_image
                    self.load_image()
                if self.side == "L":
                    self.IMG_PATH = self.stay_l_image
                    self.load_image()
            elif self.enemy_animation_counter < 10*4 and (self.enemy_animation_counter % 10) == 0 and self.enemy_move_counter < 200-40:
                if self.side == "R":
                    self.IMG_PATH = self.animation_walk_r_list[self.enemy_animation_counter//10]
                    self.load_image()
                if self.side == "L":
                    self.IMG_PATH = self.animation_walk_l_list[self.enemy_animation_counter//10]
                    self.load_image()
            elif self.enemy_animation_counter >= 10*4:
                self.enemy_animation_counter = -1
        self.enemy_animation_counter += 1
#dummy = Enemy(SPEED = 0, TYPE = "dummy", HP = 100, DAMAGE = 0, x = 0, y = 0, width = 20, height = 75, img_path = 'images/enemy_image.png' )
#
#
#enemy1 = Enemy(SPEED = 5, TYPE = "swordsman", HP = 50, DAMAGE = 10, x = 450, y = 30, width = 70, height = 70, img_path = 'images/enemy_image.png' )


