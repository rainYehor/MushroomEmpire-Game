import pygame
from moviepy.editor import *
from modules import *
from models import *
from main_hero import *
from enemy import *

loading = VideoFileClip("video/loadingscreen.mp4")
vid = loading.subclip(0,5)

end = VideoFileClip("video/титры.mp4")
end = end.subclip(1)

pygame.init()
pygame.display.set_caption("Mushroom Empire")


clock = pygame.time.Clock()


font = pygame.font.SysFont("Impact", 20)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def game_loop():  
    game = True
    scene = "menu"
    
    
    MUSIK_STATUS = True
    #SOUND_STATUS = True

    dict_objects = create_map(levels[main_hero.current_level])
    pygame.mixer.music.play(-1)
    while game:
        #print(clock.get_fps())
        BACKGROUNDS_PATH[scene].show_image(window)
        mouse_pos = pygame.mouse.get_pos()
        if main_hero.HP <= 0:
            scene = "death"
        if main_hero.dialog_readen == 16:
            scene = "end"

        if scene == 'menu':
            #menu scene
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button_start.check_click(mouse_pos) == True:
                        scene = main_hero.current_level
                        vid.preview(FPS)
                        change_music(scene,MUSIC_PATH, MUSIK_STATUS)
                    if menu_button_settings.check_click(mouse_pos) == True:
                        scene = 'settings'
                        change_music(scene,MUSIC_PATH, MUSIK_STATUS)
                    if menu_button_exit.check_click(mouse_pos) == True:
                        
                        game = False
#                    if menu_button_continue.check_click(mouse_pos) == True:
#                        pass
                    
            #menu_button_continue.show_image(window)
            menu_button_start.show_image(window)
            menu_button_settings.show_image(window)
            menu_button_exit.show_image(window)
            

            
        if scene == 0 or scene == 1:
            tsk_menu.load_image()#TEST TASK CREATOR
            tsk_menu.show_image(window)#TEST TASK CREATOR

        if scene == 0:#Training location - Тренировка
            pressed_mouse_buttons = pygame.mouse.get_pressed()
            if TASKS['tutorial']['second_task']['prog'] != True:
                tsk_menu.create_task(TASKS['tutorial']['second_task']['name'], TASKS['tutorial']['second_task']['description'], window)#TEST TASK CREATOR
                if pressed_mouse_buttons[0]:
                    TASKS['tutorial']['second_task']['prog'] = True
            
            if main_hero.current_level != scene:
                levels.remove(main_level_before)
                scene = main_hero.current_level
                dict_objects = create_map(levels[main_hero.current_level])
                vid.preview(FPS)
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
            

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
            for enemy in dict_objects["list_enemy"]:#TODO
                enemy.act(window, main_hero)
                main_hero.check_earn_damage()
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                elif isinstance(block, Shop):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == 1:#main_level
            pressed_keys = pygame.key.get_pressed()
            if TASKS['tutorial']['first_task']['prog'] != True:
                tsk_menu.create_task(TASKS['tutorial']['first_task']['name'], TASKS['tutorial']['first_task']['description'], window)#TEST TASK CREATOR
                if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_d] or pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_s]:
                    TASKS['tutorial']['first_task']['prog'] = True
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                dict_objects = create_map(levels[main_hero.current_level])
                vid.preview(FPS)
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            #
            main_hero.move(dict_objects["list_blocks"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    
            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
            main_hero.bars(window)
            
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                elif isinstance(block, Shop):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == 2:#level1 - уровень с под уровнями
            
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                vid.preview(FPS)
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            main_hero.move(dict_objects["list_blocks"])
            #main_hero.attack()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                elif isinstance(block, Shop):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == 3:#Горы
            if main_hero.current_level != scene:
                vid.preview(FPS)
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            main_hero.move(dict_objects["list_blocks"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False   

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                elif isinstance(block, Shop):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == 4:#Замок
            if main_hero.current_level != scene:
                vid.preview(FPS)
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            main_hero.move(dict_objects["list_blocks"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False   

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                elif isinstance(block, Shop):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == 5:#Замок внуитри
            if main_hero.current_level != scene:
                vid.preview(FPS)
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            main_hero.move(dict_objects["list_blocks"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False   

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == 6:#boss_level - уровень с под уровнями
            if main_hero.current_level != scene:
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()
            #boss
            if main_hero.can_move:
                dict_objects["boss"].move()
                dict_objects["boss"].shoot(main_hero, window)

            for enemy in dict_objects["list_enemy"]:
                enemy.act_chandelier_holder(main_hero.hits, dict_objects["boss"].position)
                if enemy.HP <= 0:
                    dict_objects["list_enemy"].remove(enemy)
                    dict_objects["list_objects"].remove(enemy)
                    dict_objects["list_blocks"].remove(enemy)
            dict_objects["chandelier"].check_chandelier(dict_objects["list_enemy"], dict_objects["boss"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            for obj in dict_objects["list_objects"]:
                obj.show_image(window)   
            
            for bullet in dict_objects["boss"].bullet_list:
                bullet.update(window)
                main_hero.new_HP = bullet.check_collide(main_hero.rect, main_hero.HP)
                main_hero.check_earn_damage()  
            main_hero.bars(window) 
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == "under1":#under1 - Под уровень 1
            if main_hero.current_level != scene:
                under_levels.pop(scene)

                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)
            
            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
            
            for obj in dict_objects["list_objects"]:
                obj.show_image(window)    
            for enemy in dict_objects["list_enemy"]:
                if main_hero.can_move:
                    enemy.act(window, main_hero)
                    main_hero.check_earn_damage()
                    if enemy.HP <= 0:
                        dict_objects["list_enemy"].remove(enemy)
                        dict_objects["list_objects"].remove(enemy)
                    
            
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == "under2":#under2 - Под уровень 2
            if main_hero.current_level != scene:
                under_levels.pop(scene)
                vid.preview(FPS)
                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)

            
            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()
               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                                 
            
            for obj in dict_objects["list_objects"]:
                obj.show_image(window)
            for enemy in dict_objects["list_enemy"]:
                if main_hero.can_move:
                    enemy.act(window, main_hero)
                    main_hero.check_earn_damage() 
                    if enemy.HP <= 0:
                        dict_objects["list_enemy"].remove(enemy)
                        dict_objects["list_objects"].remove(enemy)
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == "under3":#under3 - Под уровень 3
            if main_hero.current_level != scene:
                under_levels.pop(scene)
                vid.preview(FPS)

                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)
            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
            
            for obj in dict_objects["list_objects"]:
                obj.show_image(window)      
            for enemy in dict_objects["list_enemy"]:
                if main_hero.can_move:
                    enemy.act(window, main_hero)
                    main_hero.check_earn_damage()
                    if enemy.HP <= 0:
                        dict_objects["list_enemy"].remove(enemy)
                        dict_objects["list_objects"].remove(enemy)                   
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == "under4":#under3 - Под уровень 2_1
            if main_hero.current_level != scene:
                under_levels.pop(scene)
                vid.preview(FPS)

                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)
            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
            
            for obj in dict_objects["list_objects"]:
                obj.show_image(window)      
            for enemy in dict_objects["list_enemy"]:
                if main_hero.can_move:
                    enemy.act(window, main_hero)
                    main_hero.check_earn_damage()
                    if enemy.HP <= 0:
                        dict_objects["list_enemy"].remove(enemy)
                        dict_objects["list_objects"].remove(enemy)                   
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == "under5":#under3 - Под уровень 2_2
            if main_hero.current_level != scene:
                under_levels.pop(scene)
                vid.preview(FPS)

                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)
            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
            
            for obj in dict_objects["list_objects"]:
                obj.show_image(window)      
            for enemy in dict_objects["list_enemy"]:
                if main_hero.can_move:
                    enemy.act(window, main_hero)
                    main_hero.check_earn_damage()
                    if enemy.HP <= 0:
                        dict_objects["list_enemy"].remove(enemy)
                        dict_objects["list_objects"].remove(enemy)                   
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == "under6":#under6 - Под уровень 2_3
            if main_hero.current_level != scene:
                under_levels.pop(scene)
                vid.preview(FPS)

                scene = main_hero.current_level
                if type(main_hero.current_level) == int:
                    dict_objects = create_map(levels[main_hero.current_level])
                else:
                    dict_objects = create_map(under_levels[main_hero.current_level])
                change_music(scene,MUSIC_PATH, MUSIK_STATUS)
            main_hero.move(dict_objects["list_blocks"])
            main_hero.attack()  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
            
            for obj in dict_objects["list_objects"]:
                obj.show_image(window)      
            for enemy in dict_objects["list_enemy"]:
                if main_hero.can_move:
                    enemy.act(window, main_hero)
                    main_hero.check_earn_damage()
                    if enemy.HP <= 0:
                        dict_objects["list_enemy"].remove(enemy)
                        dict_objects["list_objects"].remove(enemy)                   
            main_hero.bars(window)
            for block in dict_objects["list_usable_blocks"]:
                if isinstance(block, Chest):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, dict_objects)
                elif isinstance(block, Vilager):
                    block.check_collide(main_hero, pygame.key.get_pressed(), window, mouse_pos)
                else:
                    block.check_collide(main_hero, pygame.key.get_pressed())
        if scene == 'settings':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if settings_button_sounds.check_click(mouse_pos):
                    #     if SOUND_STATUS == True:
                    #         settings_button_sounds.IMG_PATH = 'images/menu_button/sounds_off.png'
                    #         settings_button_sounds.load_image()
                    #         SOUND_STATUS = False

                    #     elif SOUND_STATUS == False:
                    #         settings_button_sounds.IMG_PATH = 'images/menu_button/sounds_on.png'
                    #         settings_button_sounds.load_image()
                    #         SOUND_STATUS = True

                    if settings_button_music.check_click(mouse_pos):
                        if MUSIK_STATUS == True:
                            settings_button_music.IMG_PATH = 'images/menu_button/music_off.png'
                            settings_button_music.load_image()
                            pygame.mixer.music.unload()
                            MUSIK_STATUS = False

                        elif MUSIK_STATUS == False:
                            settings_button_music.IMG_PATH = 'images/menu_button/music_on.png'
                            settings_button_music.load_image()
                            pygame.mixer.music.load('music/settings.wav')
                            pygame.mixer.music.play(-1)
                            MUSIK_STATUS = True

                    if button_back.check_click(mouse_pos) == True:
                        scene = 'menu'
                        change_music(scene,MUSIC_PATH, MUSIK_STATUS)
                    
            button_back.show_image(window)
            #settings_button_sounds.show_image(window)
            settings_button_music.show_image(window)
                 
        if scene == "death":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
        if scene == "end":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            end.preview(FPS)
            game = False

        pygame.display.flip()
        clock.tick(60)

game_loop()