import pygame
from graphic import Graphic
from settings import *
from button import Button
from sounds import sounds_shop
class Shop_button(Button):
    def __init__(self, category, selected_category_image, **kwargs):
        super().__init__(**kwargs)
        self.category = category
        self.standart_image = self.IMG_PATH
        self.selected_category_image = selected_category_image

class Product(Graphic):
    def __init__(self, price, result, **kwargs):
        super().__init__(**kwargs)
        self.price_count = price
        self.sold = False
        self.result = result
        self.buy_button = Button(x=self.rect.x+5, y=self.rect.bottom+25, width=90, height=28, img_path="images/shop_items/button_buy_green.png")
        self.buy_button_not_enough = Graphic(x=self.buy_button.rect.x, y=self.buy_button.rect.y, width=self.buy_button.rect.width, height=self.buy_button.rect.height, img_path="images/shop_items/button_buy_red.png")
        self.price = Graphic(x=self.rect.x-10, y=self.rect.bottom-10, width=self.rect.width+20, height=20, img_path=f"images/shop_items/price_{price}.png")
            
    def check_buy(self, window, main_hero, mouse, mouse_pos, sound):
        self.show_image(window)
        self.price.show_image(window)
        if self.price_count <= main_hero.money_count or self.sold == True:
            if self.buy_button.check_click(mouse_pos) and mouse and self.sold == False:
                #ifSOUND_STATUS:
                sound.play()
                if self.result == "secret":
                    pass
                elif "hp" in self.result:
                    self.result = self.result.split("+")
                    main_hero.new_HP += int(self.result[1])
                    main_hero.change_health_bar()
                elif "dmg" in self.result:
                    self.result = self.result.split("+")
                    if main_hero.damage < int(self.result[1]):
                        main_hero.damage = int(self.result[1])
                elif "arm" in self.result:
                    self.result = self.result.split("+")
                    main_hero.armor = int(self.result[1])
                main_hero.money_count -= self.price_count
                self.sold = True
                self.buy_button.IMG_PATH =  "images/shop_items/button_sold.png"
                self.buy_button.load_image()
            self.buy_button.show_image(window)
        else:
            self.buy_button_not_enough.show_image(window) 
        return main_hero

class Shop(Graphic):
    def __init__(self, categories:list, sounds, **kwargs):
        super().__init__(**kwargs)
        self.shop_background = Graphic(240, 110, SCREEN_WIDTH-(240*2), SCREEN_HEIGHT-(110*2), "images/shop_items/shop_background.png")
        self.shop_name = Graphic(self.shop_background.rect.x , self.shop_background.rect.y, self.shop_background.rect.width, 140, "images/shop_items/shop_name.png")
        self.categories = []
        self.next_x = self.shop_background.rect.x
        self.exit = Button(x = self.shop_background.rect.right - 40, y = self.shop_background.rect.top, width = 40, height = 40, img_path = "images/shop_items/exit_cross.png")
        for category in categories:
            if category == "swords":
                self.category_image = "images/shop_items/sword_category.png"
                self.selected_category_image = "images/shop_items/sword_category_selected.png"
            if category == "armors":
                self.category_image = "images/shop_items/armor_category.png"
                self.selected_category_image = "images/shop_items/armor_category_selected.png"
            if category == "potions":
                self.category_image = "images/shop_items/potion_category.png"
                self.selected_category_image = "images/shop_items/potion_category_selected.png"
            self.categories.append(Shop_button(x=self.next_x, y=self.shop_background.rect.y + self.shop_name.rect.height, width=self.shop_background.rect.width / len(categories), height=140, img_path=self.category_image, category=category, selected_category_image=self.selected_category_image))
            self.next_x += self.shop_background.rect.width / len(categories)
        self.assortment = {
            "swords": {
                "sword1":Product(x=self.shop_background.rect.x+125, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/sword_1.png", price=100, result="dmg+10"),
                "sword2":Product(x=self.shop_background.rect.x+125+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/sword_2.png", price=200, result="dmg+15"),
                "sword3":Product(x=self.shop_background.rect.x+125+100+50+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/sword_3.png", price=300, result="dmg+20"),
                "sword4":Product(x=self.shop_background.rect.x+125+100+50+100+50+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/sword_4.png", price=400, result="dmg+25")
            },
            "armors": {
                "armor1":Product(x=self.shop_background.rect.x+125, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/armor_1.png", price=100, result="arm+1"),
                "armor2":Product(x=self.shop_background.rect.x+125+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/armor_2.png", price=200, result="arm+2"),
                "armor3":Product(x=self.shop_background.rect.x+125+100+50+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/armor_3.png", price=300, result="arm+3"),
                "armor4":Product(x=self.shop_background.rect.x+125+100+50+100+50+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/armor_4.png", price=400, result="arm+5")
            },
            "potions": {
                "potion1":Product(x=self.shop_background.rect.x+125, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/potion_1.png", price=50, result="hp+3"),
                "potion2":Product(x=self.shop_background.rect.x+125+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/potion_2.png", price=100, result="hp+5"),
                "potion3":Product(x=self.shop_background.rect.x+125+100+50+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/potion_3.png", price=150, result="hp+10"),
                "potion4":Product(x=self.shop_background.rect.x+125+100+50+100+50+100+50, y=self.categories[0].rect.bottom+30, width=100, height=100, img_path="images/shop_items/potion_4.png", price=999, result="secret")
            }

        }                         
        self.current_cattegory = None
        self.darkness = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.darkness.fill((0,0,0,122))
        self.shop_isOpen = False
        self.animation_list = [
            "images/shop_items/shop_0.png",
            "images/shop_items/shop_1.png"
        ]
        self.animation_counter = 0
        self.sounds = sounds

    def check_collide(self, main_hero, keys, window, mouse_pos):

        if self.animation_counter < 40 and (self.animation_counter % 20) == 0:
            self.IMG_PATH = self.animation_list[self.animation_counter//20]
            self.load_image()
        elif self.animation_counter >= 40:
            self.animation_counter = -1
        self.animation_counter += 1

        mouse = pygame.mouse.get_pressed()[0]

        if self.exit.check_click(mouse_pos) and mouse:
            self.shop_isOpen = False
            main_hero.can_move = True

        if self.rect.colliderect(main_hero):
            if keys[pygame.K_e] and self.shop_isOpen == False:
                self.shop_isOpen = True
                main_hero.can_move = False
                #if SOUND_STATUS:
                self.sounds["shop_open"].play()

        if self.shop_isOpen:
            window.blit(self.darkness, (0, 0))
            self.shop_background.show_image(window)
            self.shop_name.show_image(window)
            self.exit.show_image(window)
            if self.current_cattegory != None:
                for product in self.assortment[self.current_cattegory]:
                    main_hero = self.assortment[self.current_cattegory][product].check_buy(window, main_hero, mouse, mouse_pos, self.sounds["shop_buy"])
                    main_hero.change_coin_bag()
            for category in self.categories:
                if self.current_cattegory == category.category:
                    category.IMG_PATH = category.selected_category_image
                    category.load_image()
                else:
                    category.IMG_PATH = category.standart_image
                    category.load_image()
                category.show_image(window)
                if category.check_click(mouse_pos) and mouse:
                    self.current_cattegory = category.category
shop = Shop(x = 0, y = 0, height = 200, width = 328, img_path = 'images/shop_items/shop_0.png', categories=["swords", "armors", "potions"], sounds=sounds_shop)