import pygame
pygame.mixer.init()
pygame.mixer.music.load("music//menu_music.wav")
pygame.mixer.music.set_volume(0.1)
def change_music(scene,file_path, music_status):
    if music_status:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(file_path[scene])
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)