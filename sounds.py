import pygame
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
walk_grass_sound = pygame.mixer.Sound("sounds/walk_grass.wav")
walk_grass_sound.set_volume(0.3)
attack_sound = pygame.mixer.Sound("sounds/Звук меча 2.wav")
attack_sound.set_volume(0.1)
door_opening_sound = pygame.mixer.Sound("sounds/Открытие двери.wav")

boss_shoot = pygame.mixer.Sound("sounds/boss_shoot.wav")
boss_ride = pygame.mixer.Sound("sounds/boss_ride.wav")

shop_buy = pygame.mixer.Sound("sounds/shop_buy.wav")
shop_open = pygame.mixer.Sound("sounds/shop_open.wav")
shop_open.set_volume(0.5)
shop_buy.set_volume(0.5)

sounds_shop = {
    "shop_buy": shop_buy,
    "shop_open": shop_open
}

sounds_boss = {
    "boss_shoot": boss_shoot,
    "boss_ride": boss_ride
}

sounds_main_hero = {
    "attack_sound": attack_sound,
    "walk_grass_sound": walk_grass_sound
}